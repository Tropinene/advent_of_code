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

func solve(graph [][]byte, moves string) int {
	rows, cols := len(graph), len(graph[0])
	curR, curC := findRobot(graph)

	for _, move := range moves {
		//fmt.Println(string(move))
		//printG(graph)
		//fmt.Println()
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

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	graphStr, moves := readFile(filepath.Join(dir, "input.txt"))
	graphStrs := strings.Split(graphStr, "\n")
	graph := make([][]byte, len(graphStrs))
	for i, str := range graphStrs {
		graph[i] = []byte(str)
	}

	p1 := solve(graph, moves)
	fmt.Println("[Part 1]:", p1)
}
