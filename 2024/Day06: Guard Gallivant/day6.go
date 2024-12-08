package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

func copyArray(original [][]byte) [][]byte {
	copyArr := make([][]byte, len(original))
	for i := range original {
		copyArr[i] = make([]byte, len(original[i]))
		copy(copyArr[i], original[i])
	}
	return copyArr
}

func readFile(fileName string) []string {
	data, err := os.ReadFile(fileName)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return []string{}
	}

	lines := strings.Split(string(data), "\n")
	return lines
}

func turn(d int) int {
	return (d + 1) % 4
}

func check(maxR, maxC, curR, curC int) bool {
	if curR >= 0 && curR < maxR && curC >= 0 && curC < maxC {
		return true
	}
	return false
}

func checkOB(arr [][]byte, d, r, c int) bool {
	rows, cols := len(arr), len(arr[0])
	tmpR, tmpC := r, c
	for check(rows, cols, tmpR, tmpC) {
		if arr[tmpR][tmpC] == '#' {
			return true
		}
		if d == 0 {
			tmpR -= 1
		} else if d == 1 {
			tmpC += 1
		} else if d == 2 {
			tmpR += 1
		} else {
			tmpC -= 1
		}
	}
	return false
}

func isLoop(arr [][]byte, r, c int) bool {
	copyArr := copyArray(arr)
	rows, cols := len(copyArr), len(copyArr[0])
	direction := 0
	lastR, lastC := r, c
	for check(rows, cols, r, c) {
		if copyArr[r][c] == '#' {
			direction = turn(direction)
			r, c = lastR, lastC
			continue
		}
		if copyArr[r][c] == 'z' {
			return true
		}
		if copyArr[r][c] == '.' {
			copyArr[r][c] = 'a'
		} else if copyArr[r][c] >= 'a' && copyArr[r][c] < 'z' {
			num := int(copyArr[r][c] - 'a')
			copyArr[r][c] = byte(num+1) + 'a'
		}

		lastR, lastC = r, c
		if direction == 0 {
			r -= 1
		} else if direction == 1 {
			c += 1
		} else if direction == 2 {
			r += 1
		} else {
			c -= 1
		}
	}
	return false
}

func solve1(arr [][]byte, r, c int) int {
	rows, cols := len(arr), len(arr[0])
	direction, res := 0, 0
	lastR, lastC := r, c
	for check(rows, cols, r, c) {
		if arr[r][c] == '#' {
			direction = turn(direction)
			r, c = lastR, lastC
			continue
		}
		if arr[r][c] == '.' {
			res += 1
			arr[r][c] = 'x'
		}

		lastR, lastC = r, c
		if direction == 0 {
			r -= 1
		} else if direction == 1 {
			c += 1
		} else if direction == 2 {
			r += 1
		} else {
			c -= 1
		}
	}
	return res
}

func solve2(arr [][]byte, r, c int) int {
	copyArr := copyArray(arr)
	rows, cols := len(arr), len(arr[0])
	direction, res := 0, 0
	lastR, lastC := r, c
	r0, c0 := r, c
	for check(rows, cols, r, c) {
		if copyArr[r][c] == '#' {
			direction = turn(direction)
			r, c = lastR, lastC
			continue
		}
		if copyArr[r][c] == '.' {
			copyArr[r][c] = 'x'
		}
		flag := checkOB(arr, turn(direction), r, c)

		lastR, lastC = r, c
		if direction == 0 {
			r -= 1
		} else if direction == 1 {
			c += 1
		} else if direction == 2 {
			r += 1
		} else {
			c -= 1
		}
		if flag && check(rows, cols, r, c) && arr[r][c] != '#' {
			arr[r][c] = '#'
			if isLoop(arr, r0, c0) {
				res++
			}
			arr[r][c] = '.'
		}
	}
	return res
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))
	r, c, flag := 0, 0, false
	var arr [][]byte
	for i, line := range lines {
		arr = append(arr, []byte(line))
		if !flag {
			for j, char := range line {
				if char == '^' {
					r, c = i, j
					flag = true
					arr[r][c] = '.'
				}
			}
		}
	}
	p1 := solve1(arr, r, c)
	p2 := solve2(arr, r, c)
	fmt.Printf("[Part1] : %d\n", p1)
	fmt.Printf("[Part2] : %d\n", p2) // wrong
}
