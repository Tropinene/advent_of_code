package main

import (
	"container/heap"
	"fmt"
	"math"
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

const (
	East  = 0
	South = 1
	West  = 2
	North = 3
)

var directions = [][]int{
	{0, 1},  // East
	{1, 0},  // South
	{0, -1}, // West
	{-1, 0}, // North
}

type State struct {
	cost      int
	row, col  int
	direction int
	index     int
}

type PriorityQueue []*State

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].cost < pq[j].cost
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*State)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil  // avoid memory leak
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

type Position struct {
	row, col int
}

func findStartAndEnd(mazeLines []string) (Position, Position, bool) {
	var start, end Position
	startFound, endFound := false, false

	for r := range mazeLines {
		for c := range mazeLines[r] {
			switch mazeLines[r][c] {
			case 'S':
				start = Position{r, c}
				startFound = true
			case 'E':
				end = Position{r, c}
				endFound = true
			}
		}
	}
	return start, end, startFound && endFound
}

func initDistanceArray(rows, cols int) [][][]int {
	dist := make([][][]int, rows)
	for i := range dist {
		dist[i] = make([][]int, cols)
		for j := range dist[i] {
			dist[i][j] = make([]int, 4)
			for k := range dist[i][j] {
				dist[i][j][k] = math.MaxInt32
			}
		}
	}
	return dist
}

func initPriorityQueue(start Position) PriorityQueue {
	pq := make(PriorityQueue, 0)
	heap.Init(&pq)
	heap.Push(&pq, &State{
		cost:      0,
		row:       start.row,
		col:       start.col,
		direction: East,
	})
	return pq
}

func isValidMove(row, col, rows, cols int, mazeLines []string) bool {
	return row >= 0 && row < rows && col >= 0 && col < cols && mazeLines[row][col] != '#'
}

func tryMove(current *State, dist [][][]int, pq *PriorityQueue, rows, cols int, mazeLines []string) {
	dr, dc := directions[current.direction][0], directions[current.direction][1]
	newRow, newCol := current.row+dr, current.col+dc

	if isValidMove(newRow, newCol, rows, cols, mazeLines) {
		newCost := current.cost + 1
		if newCost < dist[newRow][newCol][current.direction] {
			dist[newRow][newCol][current.direction] = newCost
			heap.Push(pq, &State{
				cost:      newCost,
				row:       newRow,
				col:       newCol,
				direction: current.direction,
			})
		}
	}
}

func tryTurn(current *State, dist [][][]int, pq *PriorityQueue) {
	for _, turn := range []int{-1, 1} {
		newDir := (current.direction + turn + 4) % 4
		newCost := current.cost + 1000
		if newCost < dist[current.row][current.col][newDir] {
			dist[current.row][current.col][newDir] = newCost
			heap.Push(pq, &State{
				cost:      newCost,
				row:       current.row,
				col:       current.col,
				direction: newDir,
			})
		}
	}
}

func findPath(mazeLines []string, pq PriorityQueue, dist [][][]int, end Position) int {
	rows, cols := len(mazeLines), len(mazeLines[0])
	visited := make(map[string]bool)

	for pq.Len() > 0 {
		current := heap.Pop(&pq).(*State)

		if current.row == end.row && current.col == end.col {
			return current.cost
		}

		stateKey := fmt.Sprintf("%d,%d,%d", current.row, current.col, current.direction)
		if visited[stateKey] || current.cost > dist[current.row][current.col][current.direction] {
			continue
		}
		visited[stateKey] = true

		tryMove(current, dist, &pq, rows, cols, mazeLines)
		tryTurn(current, dist, &pq)
	}
	return 0
}

func solve1(mazeLines []string) int {
	if len(mazeLines) == 0 {
		return 0
	}

	start, end, ok := findStartAndEnd(mazeLines)
	if !ok {
		return 0
	}

	dist := initDistanceArray(len(mazeLines), len(mazeLines[0]))
	dist[start.row][start.col][East] = 0
	pq := initPriorityQueue(start)

	return findPath(mazeLines, pq, dist, end)
}

type QueueState struct {
	row, col, direction int
}

func findMinCostEnd(dist [][][]int, end Position) int {
	minCostEnd := math.MaxInt32
	for d := 0; d < 4; d++ {
		if dist[end.row][end.col][d] < minCostEnd {
			minCostEnd = dist[end.row][end.col][d]
		}
	}
	return minCostEnd
}

func initBestPathQueue(dist [][][]int, end Position, minCostEnd int) ([]QueueState, map[string]bool) {
	queue := []QueueState{}
	visitedRev := make(map[string]bool)

	for d := 0; d < 4; d++ {
		if dist[end.row][end.col][d] == minCostEnd {
			state := QueueState{end.row, end.col, d}
			queue = append(queue, state)
			key := fmt.Sprintf("%d,%d,%d", end.row, end.col, d)
			visitedRev[key] = true
		}
	}
	return queue, visitedRev
}

func processPredecessors(current QueueState, dist [][][]int, rows, cols int, mazeLines []string,
	visitedRev map[string]bool, queue []QueueState, onBestPath [][]bool) []QueueState {

	costHere := dist[current.row][current.col][current.direction]
	onBestPath[current.row][current.col] = true

	dr, dc := directions[current.direction][0], directions[current.direction][1]
	rPrev, cPrev := current.row-dr, current.col-dc

	if isValidMove(rPrev, cPrev, rows, cols, mazeLines) {
		if dist[rPrev][cPrev][current.direction] == costHere-1 {
			key := fmt.Sprintf("%d,%d,%d", rPrev, cPrev, current.direction)
			if !visitedRev[key] {
				visitedRev[key] = true
				queue = append(queue, QueueState{rPrev, cPrev, current.direction})
			}
		}
	}

	for _, turn := range []int{-1, 1} {
		dPre := (current.direction + turn + 4) % 4
		if dist[current.row][current.col][dPre] == costHere-1000 {
			key := fmt.Sprintf("%d,%d,%d", current.row, current.col, dPre)
			if !visitedRev[key] {
				visitedRev[key] = true
				queue = append(queue, QueueState{current.row, current.col, dPre})
			}
		}
	}

	return queue
}

func countBestPathCells(onBestPath [][]bool) int {
	result := 0
	for r := range onBestPath {
		for c := range onBestPath[r] {
			if onBestPath[r][c] {
				result++
			}
		}
	}
	return result
}

func solve2(mazeLines []string) int {
	rows, cols := len(mazeLines), len(mazeLines[0])
	if rows == 0 {
		return 0
	}

	start, end, ok := findStartAndEnd(mazeLines)
	if !ok {
		return 0
	}

	dist := initDistanceArray(rows, cols)
	dist[start.row][start.col][East] = 0
	pq := initPriorityQueue(start)

	if findPath(mazeLines, pq, dist, end) == 0 {
		return 0
	}

	minCostEnd := findMinCostEnd(dist, end)
	if minCostEnd == math.MaxInt32 {
		return 0
	}

	onBestPath := make([][]bool, rows)
	for i := range onBestPath {
		onBestPath[i] = make([]bool, cols)
	}

	queue, visitedRev := initBestPathQueue(dist, end, minCostEnd)

	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]
		queue = processPredecessors(current, dist, rows, cols, mazeLines, visitedRev, queue, onBestPath)
	}

	return countBestPathCells(onBestPath)
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))

	p1 := solve1(lines)
	fmt.Println("[Part 1]:", p1)
	p2 := solve2(lines)
	fmt.Println("[Part 2]:", p2)
}
