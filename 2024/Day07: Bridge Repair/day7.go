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
	return strings.Split(strings.TrimSpace(string(data)), "\n")
}

func evaluateExpression(numbers []int, ops []byte) int {
	result := numbers[0]
	for i := 0; i < len(ops); i++ {
		if ops[i] == '+' {
			result += numbers[i+1]
		} else if ops[i] == '*' {
			result *= numbers[i+1]
		} else {
			resultStr := fmt.Sprintf("%d%d", result, numbers[i+1])
			result, _ = strconv.Atoi(resultStr)
		}
	}
	return result
}

func canAchieveAim(numbers []int, aim int, isPart1 bool) bool {
	if len(numbers) == 1 {
		return numbers[0] == aim
	}

	numOps := len(numbers) - 1
	if isPart1 {
		for mask := 0; mask < (1 << numOps); mask++ {
			ops := make([]byte, numOps)
			for i := 0; i < numOps; i++ {
				if (mask & (1 << i)) != 0 {
					ops[i] = '*'
				} else {
					ops[i] = '+'
				}
			}

			if evaluateExpression(numbers, ops) == aim {
				return true
			}
		}
	} else {
		for mask := 0; mask < (1 << (numOps * 2)); mask++ {
			ops := make([]byte, numOps)
			for i := 0; i < numOps; i++ {
				opCode := (mask >> (i * 2)) & 3
				if opCode == 0 {
					ops[i] = '+'
				} else if opCode == 1 {
					ops[i] = '*'
				} else {
					ops[i] = '|'
				}
			}
			if evaluateExpression(numbers, ops) == aim {
				return true
			}
		}
	}

	return false
}

func solve(lines []string) (int, int) {
	res1, res2 := 0, 0
	for _, line := range lines {
		if line == "" {
			continue
		}
		parts := strings.Split(line, ":")
		aim, _ := strconv.Atoi(strings.TrimSpace(parts[0]))

		numStrs := strings.Fields(strings.TrimSpace(parts[1]))
		numbers := make([]int, 0, len(numStrs))
		for _, numStr := range numStrs {
			if num, err := strconv.Atoi(numStr); err == nil {
				numbers = append(numbers, num)
			}
		}

		if canAchieveAim(numbers, aim, true) {
			res1 += aim
		}
		if canAchieveAim(numbers, aim, false) {
			res2 += aim
		}
	}
	return res1, res2
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))

	p1, p2 := solve(lines)
	fmt.Printf("[Part1] : %d\n", p1)
	fmt.Printf("[Part2] : %d\n", p2)
}
