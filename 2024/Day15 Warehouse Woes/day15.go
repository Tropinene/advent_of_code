package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

func readFile(fileName string) (string, string) {
	data, err := os.ReadFile(fileName)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return "", ""
	}
	tmp := strings.Split(strings.TrimSpace(string(data)), "\n\n")
	return tmp[0], tmp[1]
}

func printG(g [][]byte) {
	for _, row := range g {
		fmt.Println(string(row))
	}
}

func findRobot(graph [][]byte) (int, int) {
	rows, cols := len(graph), len(graph[0])
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if graph[i][j] == '@' {
				return i, j
			}
		}
	}
	return -1, -1
}

func countDis(graph [][]byte) int {
	rows, cols := len(graph), len(graph[0])
	count := 0
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if graph[i][j] == 'O' {
				count += i*100 + j
			}
		}
	}
	return count
}

func solve1(graph [][]byte, moves string) int {
	rows, cols := len(graph), len(graph[0])
	curR, curC := findRobot(graph)

	for _, move := range moves {
		nextC, nextR := curC, curR
		if move == '<' {
			tmp := curC - 1
			for tmp > 0 && graph[curR][tmp] == 'O' {
				tmp -= 1
			}
			if tmp == 0 || graph[curR][tmp] == '#' {
				continue
			} else {
				for tmp < curC {
					graph[curR][tmp] = graph[curR][tmp+1]
					tmp += 1
				}
				nextC -= 1
			}
		} else if move == '>' {
			tmp := curC + 1
			for tmp < cols && graph[curR][tmp] == 'O' {
				tmp += 1
			}
			if tmp == cols || graph[curR][tmp] == '#' {
				continue
			} else {
				for tmp > curC {
					graph[curR][tmp] = graph[curR][tmp-1]
					tmp -= 1
				}
				nextC += 1
			}
		} else if move == '^' {
			tmp := curR - 1
			for tmp > 0 && graph[tmp][curC] == 'O' {
				tmp -= 1
			}
			if tmp == 0 || graph[tmp][curC] == '#' {
				continue
			} else {
				for tmp < curR {
					graph[tmp][curC] = graph[tmp+1][curC]
					tmp += 1
				}
				nextR -= 1
			}
		} else if move == 'v' {
			tmp := curR + 1
			for tmp < rows && graph[tmp][curC] == 'O' {
				tmp += 1
			}
			if tmp == rows || graph[tmp][curC] == '#' {
				continue
			} else {
				for tmp > curR {
					graph[tmp][curC] = graph[tmp-1][curC]
					tmp -= 1
				}
				nextR += 1
			}
		}
		graph[curR][curC] = '.'
		curR, curC = nextR, nextC
	}
	return countDis(graph)
}

func expandMap(graph [][]byte) [][]byte {
	rows, cols := len(graph), len(graph[0])
	newGraph := make([][]byte, rows)
	for i := range newGraph {
		newGraph[i] = make([]byte, cols*2)
	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			switch graph[i][j] {
			case '#':
				newGraph[i][j*2] = '#'
				newGraph[i][j*2+1] = '#'
			case 'O':
				newGraph[i][j*2] = '['
				newGraph[i][j*2+1] = ']'
			case '.':
				newGraph[i][j*2] = '.'
				newGraph[i][j*2+1] = '.'
			case '@':
				newGraph[i][j*2] = '@'
				newGraph[i][j*2+1] = '.'
			}
		}
	}
	return newGraph
}

func countDisWide(graph [][]byte) int {
	rows, cols := len(graph), len(graph[0])
	count := 0
	for i := 0; i < rows; i++ {
		for j := 0; j < cols-1; j++ {
			if graph[i][j] == '[' && graph[i][j+1] == ']' {
				count += i*100 + j
			}
		}
	}
	return count
}

func affecting(grid [][]byte, x, y int) [][2]int {
	if grid[x][y] == '.' {
		return nil
	} else if grid[x][y] == '[' {
		return [][2]int{{x, y}, {x, y + 1}}
	} else if grid[x][y] == ']' {
		return [][2]int{{x, y}, {x, y - 1}}
	}
	return nil
}

func solve2(graph [][]byte, moves string) int {
	grid := expandMap(graph)
	//printG(grid)
	curR, curC := findRobot(grid)

	symToDir := map[rune][2]int{
		'>': {0, 1},
		'<': {0, -1},
		'^': {-1, 0},
		'v': {1, 0},
	}

	for _, move := range moves {
		dir := symToDir[move]
		newR, newC := curR+dir[0], curC+dir[1]

		if dir[0] == 0 || grid[newR][newC] == '.' {
			finalR, finalC := newR, newC

			for grid[finalR][finalC] != '.' && grid[finalR][finalC] != '#' {
				finalR, finalC = finalR+dir[0], finalC+dir[1]
			}

			if grid[finalR][finalC] != '#' {
				for finalR-dir[0] != curR || finalC-dir[1] != curC {
					grid[finalR][finalC] = grid[finalR-dir[0]][finalC-dir[1]]
					finalR, finalC = finalR-dir[0], finalC-dir[1]
				}

				grid[newR][newC] = '@'
				grid[curR][curC] = '.'
				curR, curC = newR, newC
			}
		} else if grid[newR][newC] == '#' {
			continue
		} else {
			var affectings [][][2]int
			firstAffecting := affecting(grid, newR, newC)
			affectings = append(affectings, firstAffecting)
			bad := false

			for len(affectings[len(affectings)-1]) > 0 {
				var newAffect [][2]int
				seen := make(map[[2]int]bool)
				for _, pos := range affectings[len(affectings)-1] {
					x, y := pos[0], pos[1]
					if grid[x+dir[0]][y] == '#' {
						bad = true
						break
					}
					affected := affecting(grid, x+dir[0], y)
					for _, newPos := range affected {
						if !seen[newPos] {
							seen[newPos] = true
							newAffect = append(newAffect, newPos)
						}
					}
				}
				if bad {
					break
				}
				affectings = append(affectings, newAffect)
			}

			if !bad {
				for i := len(affectings) - 1; i >= 0; i-- {
					for _, pos := range affectings[i] {
						x, y := pos[0], pos[1]
						grid[x+dir[0]][y] = grid[x][y]
						grid[x][y] = '.'
					}
				}
				grid[newR][newC] = '@'
				grid[curR][curC] = '.'
				curR, curC = newR, newC
			}
		}
		//fmt.Println("Move:", string(move))
		//printG(grid)
	}
	//printG(grid)

	return countDisWide(grid)
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	graphStr, moves := readFile(filepath.Join(dir, "input.txt"))
	graphStrs := strings.Split(graphStr, "\n")
	graph := make([][]byte, len(graphStrs))
	for i, str := range graphStrs {
		graph[i] = []byte(str)
	}
	moves = strings.ReplaceAll(moves, "\n", "")

	p1 := solve1(graph, moves)
	fmt.Println("[Part 1]:", p1)

	for i, str := range graphStrs {
		graph[i] = []byte(str)
	}
	p2 := solve2(graph, moves)
	fmt.Println("[Part 2]:", p2)
}
