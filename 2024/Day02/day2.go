package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strconv"
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

func checkSafe(reports []int) bool {
	if len(reports) <= 1 {
		return true
	}

	increasing := reports[1] > reports[0]

	for i := 1; i < len(reports); i++ {
		if increasing {
			if reports[i] <= reports[i-1] {
				return false
			}
		} else {
			if reports[i] >= reports[i-1] {
				return false
			}
		}

		diff := reports[i] - reports[i-1]
		if diff < 0 {
			diff = -diff
		}
		if diff < 1 || diff > 3 {
			return false
		}
	}
	return true
}

func checkSafe2(reports []int) bool {
	if checkSafe(reports) {
		return true
	}

	for i := 0; i < len(reports); i++ {
		newReport := make([]int, 0, len(reports)-1)
		newReport = append(newReport, reports[:i]...)
		newReport = append(newReport, reports[i+1:]...)

		if checkSafe(newReport) {
			return true
		}
	}
	return false
}

func solvePart1(reports [][]int) int {
	ans := 0
	for _, report := range reports {
		if checkSafe(report) {
			ans++
		}
	}
	return ans
}

func solvePart2(reports [][]int) int {
	ans := 0
	for _, report := range reports {
		if checkSafe2(report) {
			ans++
		}
	}
	return ans
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))
	var reports [][]int
	for _, line := range lines {
		var report []int
		tmp := strings.Split(line, " ")
		for _, v := range tmp {
			num, _ := strconv.Atoi(v)
			report = append(report, num)
		}
		reports = append(reports, report)
	}

	p1 := solvePart1(reports)
	fmt.Printf("[Part1]: %d\n", p1)
	p2 := solvePart2(reports)
	fmt.Printf("[Part2]: %d\n", p2)
}
