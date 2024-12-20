package main

import (
	"fmt"
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

	lines := strings.Split(string(data), "\n")
	return lines
}

func cntLine(arr [][]byte) int {
	res := 0
	rows, cols := len(arr), len(arr[0])
	for i := 0; i < rows; i++ {
		for j := 0; j <= cols-4; j++ {
			s := string(arr[i][j : j+4])
			if s == "XMAS" || s == "SAMX" {
				res += 1
			}
		}
	}
	return res
}

func cntCol(arr [][]byte) int {
	res := 0
	rows, cols := len(arr), len(arr[0])
	for j := 0; j < cols; j++ {
		for i := 0; i <= rows-4; i++ {
			s := string([]byte{arr[i][j], arr[i+1][j], arr[i+2][j], arr[i+3][j]})
			if s == "XMAS" || s == "SAMX" {
				res++
			}
		}
	}
	return res
}

func cntMainDiag(arr [][]byte) int {
	res := 0
	rows, cols := len(arr), len(arr[0])
	for i := 0; i <= rows-4; i++ {
		for j := 0; j <= cols-4; j++ {
			s := string([]byte{arr[i][j], arr[i+1][j+1], arr[i+2][j+2], arr[i+3][j+3]})
			if s == "XMAS" || s == "SAMX" {
				res++
			}
		}
	}
	return res
}

func cntSecondaryDiag(arr [][]byte) int {
	res := 0
	rows, cols := len(arr), len(arr[0])
	for i := 0; i <= rows-4; i++ {
		for j := 3; j < cols; j++ {
			s := string([]byte{arr[i][j], arr[i+1][j-1], arr[i+2][j-2], arr[i+3][j-3]})
			if s == "XMAS" || s == "SAMX" {
				res++
			}
		}
	}
	return res
}

func cntX_MAS(arr [][]byte) int {
	res := 0
	rows, cols := len(arr), len(arr[0])
	for i := 0; i <= rows-3; i++ {
		for j := 0; j <= cols-3; j++ {
			line1 := string([]byte{arr[i][j], arr[i][j+2]})
			line2 := string(arr[i+1][j+1])
			line3 := string([]byte{arr[i+2][j], arr[i+2][j+2]})
			if line1 == "MS" && line2 == "A" && line3 == "MS" {
				res++
			} else if line1 == "MM" && line2 == "A" && line3 == "SS" {
				res++
			} else if line1 == "SS" && line2 == "A" && line3 == "MM" {
				res++
			} else if line1 == "SM" && line2 == "A" && line3 == "SM" {
				res++
			}
		}
	}
	return res
}

func solve1(arr [][]byte) int {
	return cntLine(arr) + cntMainDiag(arr) + cntSecondaryDiag(arr) + cntCol(arr)
}

func solve2(arr [][]byte) int {
	return cntX_MAS(arr)
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))
	var arr [][]byte
	for _, line := range lines {
		arr = append(arr, []byte(line))
	}

	p1 := solve1(arr)
	p2 := solve2(arr)
	fmt.Printf("[Part 1]: %d\n", p1)
	fmt.Printf("[Part 2]: %d\n", p2)
}
