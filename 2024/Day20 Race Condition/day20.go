package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

type Position struct {
	x, y int
}

func readFile(fileName string) []string {
	data, err := os.ReadFile(fileName)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return []string{}
	}
	return strings.Split(strings.TrimSpace(string(data)), "\n")
}

func initGrid(lines []string) (Position, Position, [][]byte) {
	grid := make([][]byte, len(lines))
	var start, end Position
	findS, findE := false, false
	for i, line := range lines {
		grid[i] = []byte(line)
		if !findS || !findE {
			for j, c := range line {
				if c == 'S' && !findS {
					start = Position{i, j}
					findS = true
				}
				if c == 'E' && !findE {
					end = Position{i, j}
					findE = true
				}
			}
		}
	}
	return start, end, grid
}

func findPath(start, end Position, grid [][]byte, breakWall *Position) int {
	directions := [][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	rows, cols := len(grid), len(grid[0])

	visited := make([][]bool, rows)
	for i := range visited {
		visited[i] = make([]bool, cols)
	}

	var queue []Position
	var steps []int
	queue = append(queue, start)
	steps = append(steps, 0)
	visited[start.x][start.y] = true

	for len(queue) > 0 {
		curr := queue[0]
		currSteps := steps[0]
		queue = queue[1:]
		steps = steps[1:]

		if curr == end {
			return currSteps
		}

		for _, dir := range directions {
			next := Position{curr.x + dir[0], curr.y + dir[1]}
			if next.x < 0 || next.x >= rows || next.y < 0 || next.y >= cols || visited[next.x][next.y] {
				continue
			}

			// Check if this position is where we want to break the wall
			canMove := grid[next.x][next.y] == '.' || grid[next.x][next.y] == 'E' ||
				(breakWall != nil && next == *breakWall)

			if canMove {
				queue = append(queue, next)
				steps = append(steps, currSteps+1)
				visited[next.x][next.y] = true
			}
		}
	}

	return -1
}

func solve1(start, end Position, grid [][]byte) int {
	ans := 0
	originalLength := findPath(start, end, grid, nil)
	rows, cols := len(grid), len(grid[0])

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if grid[i][j] == '#' {
				breakPos := Position{i, j}
				newLength := findPath(start, end, grid, &breakPos)

				if newLength != -1 {
					saved := originalLength - newLength
					if saved >= 100 {
						ans += 1
					}
				}
			}
		}
	}

	return ans
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))

	start, end, grid := initGrid(lines)

	p1 := solve1(start, end, grid)
	fmt.Println("[Part 1]:", p1)
}
