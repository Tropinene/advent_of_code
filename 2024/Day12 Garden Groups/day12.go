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

func bfs(grid [][]rune, visited [][]bool, startI, startJ int) (int, int) {
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	target := grid[startI][startJ]
	queue := [][2]int{{startI, startJ}}
	visited[startI][startJ] = true

	area, perimeter := 0, 0
	for len(queue) > 0 {
		i, j := queue[0][0], queue[0][1]
		queue = queue[1:]
		area++

		edges := 4
		for _, dir := range dirs {
			ni, nj := i+dir[0], j+dir[1]
			if ni >= 0 && ni < len(grid) && nj >= 0 && nj < len(grid[0]) {
				if grid[ni][nj] == target {
					edges--
					if !visited[ni][nj] {
						visited[ni][nj] = true
						queue = append(queue, [2]int{ni, nj})
					}
				}
			}
		}
		perimeter += edges
	}
	return area, perimeter
}

func solve1(lines []string) int {
	grid := make([][]rune, len(lines))
	for i, line := range lines {
		grid[i] = []rune(line)
	}

	visited := make([][]bool, len(grid))
	for i := range visited {
		visited[i] = make([]bool, len(grid[0]))
	}

	result := 0
	for i := range grid {
		for j := range grid[i] {
			if !visited[i][j] {
				area, perimeter := bfs(grid, visited, i, j)
				result += area * perimeter
			}
		}
	}
	return result
}

func bfs2(grid [][]rune, visited [][]bool, startI, startJ int) (area int, sides int) {
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	target := grid[startI][startJ]
	queue := [][2]int{{startI, startJ}}
	visited[startI][startJ] = true

	points := make(map[[2]int]bool)

	for len(queue) > 0 {
		i, j := queue[0][0], queue[0][1]
		queue = queue[1:]
		area++
		points[[2]int{i, j}] = true

		for _, dir := range dirs {
			ni, nj := i+dir[0], j+dir[1]
			if ni >= 0 && ni < len(grid) && nj >= 0 && nj < len(grid[0]) {
				if grid[ni][nj] == target {
					if !visited[ni][nj] {
						visited[ni][nj] = true
						queue = append(queue, [2]int{ni, nj})
					}
				}
			}
		}
	}

	sides = countSides(points)
	return
}

func countSides(points map[[2]int]bool) int {
	sides := 0
	// todo
	return sides
}

func solve2(lines []string) int {
	grid := make([][]rune, len(lines))
	for i, line := range lines {
		grid[i] = []rune(line)
	}

	visited := make([][]bool, len(grid))
	for i := range visited {
		visited[i] = make([]bool, len(grid[0]))
	}

	result := 0
	for i := range grid {
		for j := range grid[i] {
			if !visited[i][j] {
				area, sides := bfs2(grid, visited, i, j)
				fmt.Println(area, sides)
				result += area * sides
			}
		}
	}
	return result
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))

	p1 := solve1(lines)
	fmt.Printf("[Part1] : %d\n", p1)
	p2 := solve2(lines)
	fmt.Printf("[Part2] : %d\n", p2)
}
