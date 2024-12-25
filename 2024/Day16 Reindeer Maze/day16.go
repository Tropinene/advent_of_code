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

// Direction constants
const (
	East  = 0
	South = 1
	West  = 2
	North = 3
)

// Directions represents the movement in (row, col) for each direction
var directions = [][]int{
	{0, 1},  // East
	{1, 0},  // South
	{0, -1}, // West
	{-1, 0}, // North
}

// State represents a state in the maze
type State struct {
	cost      int
	row, col  int
	direction int
	index     int // needed by heap.Interface
}

// PriorityQueue implementation
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

func solve1(mazeLines []string) int {
	rows := len(mazeLines)
	if rows == 0 {
		return 0
	}
	cols := len(mazeLines[0])

	// Find start and end positions
	var start, end struct{ row, col int }
	startFound, endFound := false, false

	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			switch mazeLines[r][c] {
			case 'S':
				start.row, start.col = r, c
				startFound = true
			case 'E':
				end.row, end.col = r, c
				endFound = true
			}
		}
	}

	if !startFound || !endFound {
		return 0
	}

	// Initialize distance array
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

	// Initialize starting state (facing East)
	startDir := East
	dist[start.row][start.col][startDir] = 0

	// Initialize priority queue
	pq := make(PriorityQueue, 0)
	heap.Init(&pq)
	heap.Push(&pq, &State{
		cost:      0,
		row:       start.row,
		col:       start.col,
		direction: startDir,
	})

	// Keep track of visited states
	visited := make(map[string]bool)

	// Dijkstra's algorithm
	for pq.Len() > 0 {
		current := heap.Pop(&pq).(*State)

		// If we've reached the end
		if current.row == end.row && current.col == end.col {
			return current.cost
		}

		// Create unique key for visited state
		stateKey := fmt.Sprintf("%d,%d,%d", current.row, current.col, current.direction)
		if visited[stateKey] {
			continue
		}
		visited[stateKey] = true

		if current.cost > dist[current.row][current.col][current.direction] {
			continue
		}

		// Try moving forward
		dr, dc := directions[current.direction][0], directions[current.direction][1]
		newRow, newCol := current.row+dr, current.col+dc

		if newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols &&
			mazeLines[newRow][newCol] != '#' {
			newCost := current.cost + 1
			if newCost < dist[newRow][newCol][current.direction] {
				dist[newRow][newCol][current.direction] = newCost
				heap.Push(&pq, &State{
					cost:      newCost,
					row:       newRow,
					col:       newCol,
					direction: current.direction,
				})
			}
		}

		// Try turning left
		leftDir := (current.direction - 1 + 4) % 4
		newCost := current.cost + 1000
		if newCost < dist[current.row][current.col][leftDir] {
			dist[current.row][current.col][leftDir] = newCost
			heap.Push(&pq, &State{
				cost:      newCost,
				row:       current.row,
				col:       current.col,
				direction: leftDir,
			})
		}

		// Try turning right
		rightDir := (current.direction + 1) % 4
		newCost = current.cost + 1000
		if newCost < dist[current.row][current.col][rightDir] {
			dist[current.row][current.col][rightDir] = newCost
			heap.Push(&pq, &State{
				cost:      newCost,
				row:       current.row,
				col:       current.col,
				direction: rightDir,
			})
		}
	}

	return 0
}

func solve2(mazeLines []string) int {
	rows := len(mazeLines)
	if rows == 0 {
		return 0
	}
	cols := len(mazeLines[0])

	// Find start and end positions
	var start, end struct{ row, col int }
	startFound, endFound := false, false

	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			switch mazeLines[r][c] {
			case 'S':
				start.row, start.col = r, c
				startFound = true
			case 'E':
				end.row, end.col = r, c
				endFound = true
			}
		}
	}

	if !startFound || !endFound {
		return 0
	}

	// Initialize distance array
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

	// Initialize starting state (facing East)
	startDir := East
	dist[start.row][start.col][startDir] = 0

	// Initialize priority queue for Dijkstra
	pq := make(PriorityQueue, 0)
	heap.Init(&pq)
	heap.Push(&pq, &State{
		cost:      0,
		row:       start.row,
		col:       start.col,
		direction: startDir,
	})

	visited := make(map[string]bool)

	// Run Dijkstra's algorithm
	for pq.Len() > 0 {
		current := heap.Pop(&pq).(*State)

		stateKey := fmt.Sprintf("%d,%d,%d", current.row, current.col, current.direction)
		if visited[stateKey] {
			continue
		}
		visited[stateKey] = true

		if current.cost > dist[current.row][current.col][current.direction] {
			continue
		}

		// Try moving forward
		dr, dc := directions[current.direction][0], directions[current.direction][1]
		newRow, newCol := current.row+dr, current.col+dc

		if newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols &&
			mazeLines[newRow][newCol] != '#' {
			newCost := current.cost + 1
			if newCost < dist[newRow][newCol][current.direction] {
				dist[newRow][newCol][current.direction] = newCost
				heap.Push(&pq, &State{
					cost:      newCost,
					row:       newRow,
					col:       newCol,
					direction: current.direction,
				})
			}
		}

		// Try turning left
		leftDir := (current.direction - 1 + 4) % 4
		newCost := current.cost + 1000
		if newCost < dist[current.row][current.col][leftDir] {
			dist[current.row][current.col][leftDir] = newCost
			heap.Push(&pq, &State{
				cost:      newCost,
				row:       current.row,
				col:       current.col,
				direction: leftDir,
			})
		}

		// Try turning right
		rightDir := (current.direction + 1) % 4
		newCost = current.cost + 1000
		if newCost < dist[current.row][current.col][rightDir] {
			dist[current.row][current.col][rightDir] = newCost
			heap.Push(&pq, &State{
				cost:      newCost,
				row:       current.row,
				col:       current.col,
				direction: rightDir,
			})
		}
	}

	// Find minimal cost to reach end (over all directions)
	minCostEnd := math.MaxInt32
	for d := 0; d < 4; d++ {
		if dist[end.row][end.col][d] < minCostEnd {
			minCostEnd = dist[end.row][end.col][d]
		}
	}

	if minCostEnd == math.MaxInt32 {
		return 0 // No path found
	}

	// Mark cells that lie on best paths using BFS
	onBestPath := make([][]bool, rows)
	for i := range onBestPath {
		onBestPath[i] = make([]bool, cols)
	}

	// Queue for reverse BFS
	type QueueState struct {
		row, col, direction int
	}
	queue := make([]QueueState, 0)
	visitedRev := make(map[string]bool)

	// Add all ending states with minimal cost
	for d := 0; d < 4; d++ {
		if dist[end.row][end.col][d] == minCostEnd {
			state := QueueState{end.row, end.col, d}
			queue = append(queue, state)
			key := fmt.Sprintf("%d,%d,%d", end.row, end.col, d)
			visitedRev[key] = true
		}
	}

	// Reverse BFS
	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]

		onBestPath[current.row][current.col] = true
		costHere := dist[current.row][current.col][current.direction]

		// Check predecessor by forward movement
		dr, dc := directions[current.direction][0], directions[current.direction][1]
		rPrev, cPrev := current.row-dr, current.col-dc
		if rPrev >= 0 && rPrev < rows && cPrev >= 0 && cPrev < cols {
			if mazeLines[rPrev][cPrev] != '#' {
				if dist[rPrev][cPrev][current.direction] == costHere-1 {
					key := fmt.Sprintf("%d,%d,%d", rPrev, cPrev, current.direction)
					if !visitedRev[key] {
						visitedRev[key] = true
						queue = append(queue, QueueState{rPrev, cPrev, current.direction})
					}
				}
			}
		}

		// Check predecessors by turning
		for _, dPre := range []int{(current.direction - 1 + 4) % 4, (current.direction + 1) % 4} {
			if dist[current.row][current.col][dPre] == costHere-1000 {
				key := fmt.Sprintf("%d,%d,%d", current.row, current.col, dPre)
				if !visitedRev[key] {
					visitedRev[key] = true
					queue = append(queue, QueueState{current.row, current.col, dPre})
				}
			}
		}
	}

	// Count marked cells
	result := 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if onBestPath[r][c] {
				result++
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
	fmt.Println("[Part 1]:", p1)
	p2 := solve2(lines)
	fmt.Println("[Part 2]:", p2)
}
