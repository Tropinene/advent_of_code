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

func initGrid(lines []string) ([2]int, [2]int, [][]byte) {
	grid := make([][]byte, len(lines))
	var start, end [2]int
	findS, findE := false, false
	for i, line := range lines {
		grid[i] = []byte(line)
		if !findS || !findE {
			for j, c := range line {
				if c == 'S' && !findS {
					start = [2]int{i, j}
					findS = true
				}
				if c == 'E' && !findE {
					end = [2]int{i, j}
					findE = true
				}
			}
		}
	}
	return start, end, grid
}

func printGrid(grid [][]byte, visited [][]bool) {
	for i, row := range grid {
		for j, c := range row {
			if visited[i][j] {
				fmt.Print("X")
			} else {
				fmt.Print(string(c))
			}
		}
		fmt.Println()
	}
}

func dontCheat(start, end [2]int, grid [][]byte) int {
	directions := [4][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	currX, currY := start[0], start[1]
	rows, cols := len(grid), len(grid[0])

	var visited [][]bool
	for i := 0; i < rows; i++ {
		visited = append(visited, make([]bool, cols))
	}
	//printGrid(grid, visited)

	steps := 0
	for !(currX == end[0] && currY == end[1]) {
		visited[currX][currY] = true
		for _, dir := range directions {
			nextX, nextY := currX+dir[0], currY+dir[1]
			if !visited[nextX][nextY] && nextX > 0 && nextX < rows && nextY > 0 && nextY < cols {
				if grid[nextX][nextY] == '.' || grid[nextX][nextY] == 'E' {
					currX, currY = nextX, nextY
					steps += 1
					break
				}
			}
		}
	}
	//printGrid(grid, visited)
	return steps
}

func solve1(start, end [2]int, grid [][]byte) int {
	racetrack := dontCheat(start, end, grid)
	fmt.Println(racetrack)
	return 0
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))

	start, end, grid := initGrid(lines)

	p1 := solve1(start, end, grid)
	fmt.Println("[Part 1]:", p1)
}
