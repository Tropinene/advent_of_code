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
	return strings.Split(strings.TrimSpace(string(data)), "\n\n")
}

func solve1(towels []string, designs []string) int {
	towelMap := make(map[string]bool)
	for _, t := range towels {
		towelMap[t] = true
	}

	cnt := 0
	for _, design := range designs {
		dp := make([]bool, len(design)+1)
		dp[0] = true

		for j := 1; j <= len(design); j++ {
			for k := 0; k < j; k++ {
				if dp[k] && towelMap[design[k:j]] {
					dp[j] = true
					break
				}
			}
		}

		if dp[len(design)] {
			cnt++
		}
	}

	return cnt
}

func solve2(towels []string, designs []string) int {
	towelMap := make(map[string]bool)
	for _, t := range towels {
		towelMap[t] = true
	}

	totalWays := 0

	for _, design := range designs {
		dp := make([]int, len(design)+1)
		dp[0] = 1

		for j := 1; j <= len(design); j++ {
			for k := 0; k < j; k++ {
				if dp[k] > 0 && towelMap[design[k:j]] {
					dp[j] += dp[k]
				}
			}
		}

		totalWays += dp[len(design)]
	}

	return totalWays
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))
	part1, part2 := lines[0], lines[1]

	towels := strings.Split(part1, ", ")
	designs := strings.Split(part2, "\n")

	p1 := solve1(towels, designs)
	fmt.Println("[Part 1]:", p1)
	p2 := solve2(towels, designs)
	fmt.Println("[Part 2]:", p2)
}
