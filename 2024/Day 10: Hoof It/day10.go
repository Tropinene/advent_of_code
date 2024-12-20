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
	return strings.Split(strings.TrimSpace(string(data)), "\n")
}

func findPath(topmap [][]int, r, c int) int {
	m, n := len(topmap), len(topmap[0])
	directions := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	visited := make(map[string]bool)

	var dfs func(curR, curC int) int
	dfs = func(curR, curC int) int {
		key := fmt.Sprintf("%d,%d", curR, curC)
		if visited[key] {
			return 0
		}

		// If we reach a peak (9), count it
		if topmap[curR][curC] == 9 {
			visited[key] = true
			return 1
		}

		visited[key] = true
		count := 0

		// Try all four directions
		for _, dir := range directions {
			newR, newC := curR+dir[0], curC+dir[1]

			// Check bounds
			if newR < 0 || newR >= m || newC < 0 || newC >= n {
				continue
			}

			// Can only move to positions with height = current + 1
			if topmap[newR][newC] == topmap[curR][curC]+1 {
				count += dfs(newR, newC)
			}
		}

		return count
	}

	return dfs(r, c)
}

func solve1(topmap, trailheads [][]int) int {
	ans := 0
	for _, trainhead := range trailheads {
		r, c := trainhead[0], trainhead[1]
		ans += findPath(topmap, r, c)
	}
	return ans
}

func findPath2(topmap [][]int, r, c int) int {
	m, n := len(topmap), len(topmap[0])
	directions := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}

	var dfs func(curR, curC int) int
	dfs = func(curR, curC int) int {
		if topmap[curR][curC] == 9 {
			return 1
		}

		visited[curR][curC] = true
		pathCount := 0

		for _, dir := range directions {
			newR, newC := curR+dir[0], curC+dir[1]
			if newR < 0 || newR >= m || newC < 0 || newC >= n {
				continue
			}
			if !visited[newR][newC] && topmap[newR][newC] == topmap[curR][curC]+1 {
				pathCount += dfs(newR, newC)
			}
		}
		visited[curR][curC] = false
		return pathCount
	}
	return dfs(r, c)
}

func solve2(topmap, trailheads [][]int) int {
	ans := 0
	for _, trainhead := range trailheads {
		r, c := trainhead[0], trainhead[1]
		ans += findPath2(topmap, r, c)
	}
	return ans
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))
	var topmap [][]int
	var trailheads [][]int
	// create topographic map and record the position of trailhead
	for i, line := range lines {
		var tmpLine []int
		for j, char := range line {
			num := int(char - '0')
			if num == 0 {
				trailheads = append(trailheads, []int{i, j})
			}
			tmpLine = append(tmpLine, num)
		}
		topmap = append(topmap, tmpLine)
	}

	p1 := solve1(topmap, trailheads)
	fmt.Printf("[Part1] : %d\n", p1)
	p2 := solve2(topmap, trailheads)
	fmt.Printf("[Part1] : %d\n", p2)
}
