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

func bfs(grid [][]int) int {
	rows, cols := len(grid), len(grid[0])
	directions := [4][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

	if grid[0][0] == 1 || grid[rows-1][cols-1] == 1 {
		return -1
	}

	// Create queue for BFS
	type point struct {
		x, y, dist int
	}
	queue := []point{{0, 0, 0}}

	// Create visited array
	visited := make([][]bool, rows)
	for i := range visited {
		visited[i] = make([]bool, cols)
	}
	visited[0][0] = true

	// BFS
	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]

		// If reached destination
		if curr.x == rows-1 && curr.y == cols-1 {
			return curr.dist
		}

		// Try all 4 directions
		for _, dir := range directions {
			nextX := curr.x + dir[0]
			nextY := curr.y + dir[1]

			// Check if next position is valid
			if nextX >= 0 && nextX < rows &&
				nextY >= 0 && nextY < cols &&
				!visited[nextX][nextY] &&
				grid[nextX][nextY] == 0 {

				visited[nextX][nextY] = true
				queue = append(queue, point{nextX, nextY, curr.dist + 1})
			}
		}
	}

	// No path found
	return -1
}

func solve1(rows, cols int, brokens [][2]int) int {
	grid := make([][]int, rows)
	for i := range grid {
		grid[i] = make([]int, cols)
	}

	for _, broken := range brokens {
		//fmt.Println(broken)
		grid[broken[0]][broken[1]] = 1
	}

	return bfs(grid)
}

func solve2(rows, cols int, brokens [][2]int) string {
	l := len(brokens)
	grid := make([][]int, rows)
	for i := range grid {
		grid[i] = make([]int, cols)
	}

	for i := 0; i <= 12; i++ {
		broken := brokens[i]
		grid[broken[0]][broken[1]] = 1
	}

	for i := 13; i < l; i++ {
		broken := brokens[i]
		grid[broken[0]][broken[1]] = 1
		if bfs(grid) == -1 {
			return fmt.Sprintf("%d,%d", broken[0], broken[1])
		}
	}
	return ""
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))

	var brokenPixels [][2]int
	for _, line := range lines {
		tmp := strings.Split(line, ",")
		x, _ := strconv.Atoi(tmp[0])
		y, _ := strconv.Atoi(tmp[1])
		brokenPixels = append(brokenPixels, [2]int{x, y})
	}

	// Part 1
	p1 := solve1(71, 71, brokenPixels[:1024])
	fmt.Println("[Part 1]:", p1)
	// Part 2
	p2 := solve2(71, 71, brokenPixels)
	fmt.Println("[Part 2]:", p2)
}
