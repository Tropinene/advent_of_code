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

func solve2(graph [][]byte, moves string) int {
	expandedGraph := expandMap(graph)

	rows, cols := len(expandedGraph), len(expandedGraph[0])
	curR, curC := findRobot(expandedGraph)

	for _, move := range moves {
		printG(expandedGraph)
		fmt.Println()
		nextC, nextR := curC, curR
		if move == '<' {
			tmp := curC - 1
			for tmp > 0 && (expandedGraph[curR][tmp] == '[' || expandedGraph[curR][tmp] == ']') {
				tmp -= 1
			}
			if tmp == 0 || expandedGraph[curR][tmp] == '#' {
				continue
			} else {
				for tmp < curC {
					expandedGraph[curR][tmp] = expandedGraph[curR][tmp+1]
					tmp += 1
				}
				nextC -= 1
			}
		} else if move == '>' {
			tmp := curC + 1
			for tmp < cols && (expandedGraph[curR][tmp] == '[' || expandedGraph[curR][tmp] == ']') {
				tmp += 1
			}
			if tmp == cols || expandedGraph[curR][tmp] == '#' {
				continue
			} else {
				for tmp > curC {
					expandedGraph[curR][tmp] = expandedGraph[curR][tmp-1]
					tmp -= 1
				}
				nextC += 1
			}
		} else if move == '^' {
			tmp := curR - 1
			for tmp > 0 && (expandedGraph[tmp][curC] == '[' || expandedGraph[tmp][curC] == ']') {
				tmp -= 1
			}
			if tmp == 0 || expandedGraph[tmp][curC] == '#' {
				continue
			} else {
				// todo: fix this
			}
		} else if move == 'v' {
			tmp := curR + 1
			for tmp < rows && (expandedGraph[tmp][curC] == '[' || expandedGraph[tmp][curC] == ']') {
				tmp += 1
			}
			if tmp == rows || expandedGraph[tmp][curC] == '#' {
				continue
			} else {
				// todo fix this
			}
		}
		expandedGraph[curR][curC] = '.'
		curR, curC = nextR, nextC
	}
	return countDisWide(expandedGraph)
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

	p1 := solve1(graph, moves)
	fmt.Println("[Part 1]:", p1)
	//p2 := solve2(graph, moves)
	tmpG := [][]byte{
		[]byte("####################"),
		[]byte("##[].......[].[][]##"),
		[]byte("##[]...........[].##"),
		[]byte("##[]........[][][]##"),
		[]byte("##[]......[]....[]##"),
		[]byte("##..##......[]....##"),
		[]byte("##..[]............##"),
		[]byte("##..@......[].[][]##"),
		[]byte("##......[][]..[]..##"),
		[]byte("####################"),
	}
	p2 := countDisWide(tmpG)
	fmt.Println("[Part 2]:", p2)
}
