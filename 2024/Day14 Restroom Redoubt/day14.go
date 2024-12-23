package main

import (
	"fmt"
	"math"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

func readFile(fileName string) []string {
	data, err := os.ReadFile(fileName)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return []string{}
	}
	return strings.Split(strings.TrimSpace(string(data)), "\n")
}

func extractNumbers(s string) [2]int {
	var numbers [2]int
	var currentNum, index int
	var hasNum bool

	negFlag := false
	for _, c := range s {
		if c == '-' {
			negFlag = true
		} else if c >= '0' && c <= '9' {
			currentNum = currentNum*10 + int(c-'0')
			hasNum = true
		} else {
			if hasNum {
				if negFlag {
					currentNum = -currentNum
				}
				numbers[index] = currentNum
				index++
				currentNum = 0
				negFlag = false
				hasNum = false
			}
		}
	}
	if hasNum {
		if negFlag {
			currentNum = -currentNum
		}
		numbers[index] = currentNum
	}

	return numbers
}

func solve1(ps, vs [][2]int, time int) int {
	rows, cols := 103, 101
	l := len(ps)
	a, b, c, d := 0, 0, 0, 0
	for i := 0; i < l; i++ {
		p, v := ps[i], vs[i]
		p = [2]int{
			((p[0]+v[0]*time)%cols + cols) % cols,
			((p[1]+v[1]*time)%rows + rows) % rows,
		}

		if p[0] < cols/2 && p[1] < rows/2 {
			a++
		} else if p[0] > cols/2 && p[1] < rows/2 {
			b++
		} else if p[0] < cols/2 && p[1] > rows/2 {
			c++
		} else if p[0] > cols/2 && p[1] > rows/2 {
			d++
		}
	}
	return a * b * c * d
}

func solve2(ps, vs [][2]int) int {
	bestTime := 0
	minPoints := math.MaxInt
	for t := 0; t < 10000; t++ {
		points := solve1(ps, vs, t)
		if points < minPoints && points > 0 {
			minPoints = points
			bestTime = t
		}
	}
	return bestTime
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))

	var pos, vec [][2]int
	for _, line := range lines {
		lst := strings.Split(line, " ")
		if len(lst) < 2 {
			fmt.Println("Invalid input line:", line)
			continue
		}
		p, v := extractNumbers(lst[0]), extractNumbers(lst[1])
		pos = append(pos, p)
		vec = append(vec, v)
	}
	p1 := solve1(pos, vec, 100)
	fmt.Println("[Part 1] :", p1)
	p2 := solve2(pos, vec)
	fmt.Println("[Part 2] :", p2)
}
