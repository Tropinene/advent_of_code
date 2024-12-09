package main

import (
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

func distance(x1, y1, x2, y2 int) float64 {
	dx := float64(x2 - x1)
	dy := float64(y2 - y1)
	return math.Sqrt(dx*dx + dy*dy)
}

func collinear(x1, y1, x2, y2, x3, y3 int) bool {
	area := x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
	return area == 0
}

func solve1(rows, cols int, hash map[byte][][]int) int {
	res := 0
	antinodes := make(map[string]bool)
	for _, antennas := range hash {
		l := len(antennas)
		for i := 0; i < l; i++ {
			for j := i + 1; j < l; j++ {
				x1, y1 := antennas[i][0], antennas[i][1]
				x2, y2 := antennas[j][0], antennas[j][1]

				for x := 0; x < rows; x++ {
					for y := 0; y < cols; y++ {
						d1 := distance(x, y, x1, y1)
						d2 := distance(x, y, x2, y2)

						if (d1 == d2*2 || d2 == d1*2) && (x-x1)*(y-y2) == (x-x2)*(y-y1) {
							pos := fmt.Sprintf("%d,%d", x, y)
							antinodes[pos] = true
						}
						if collinear(x, y, x1, y1, x2, y2) {
							res++
						}
					}
				}
			}
		}
	}
	return len(antinodes)
}

func solve2(rows, cols int, hash map[byte][][]int) int {
	antinodes := make(map[string]bool)

	for _, antennas := range hash {
		if len(antennas) < 2 {
			continue
		}

		for x := 0; x < rows; x++ {
			for y := 0; y < cols; y++ {
				for i := 0; i < len(antennas); i++ {
					for j := i + 1; j < len(antennas); j++ {
						x1, y1 := antennas[i][0], antennas[i][1]
						x2, y2 := antennas[j][0], antennas[j][1]

						if collinear(x1, y1, x2, y2, x, y) {
							pos := fmt.Sprintf("%d,%d", x, y)
							antinodes[pos] = true
							break
						}
					}
				}
			}
		}
	}
	return len(antinodes)
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))
	var arr [][]byte
	for _, line := range lines {
		arr = append(arr, []byte(line))
	}

	hash := make(map[byte][][]int)
	rows, cols := len(arr), len(arr[0])
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if arr[i][j] != '.' {
				tmp := arr[i][j]
				if _, ok := hash[tmp]; !ok {
					hash[tmp] = [][]int{{i, j}}
				} else {
					hash[tmp] = append(hash[tmp], []int{i, j})
				}
			}
		}
	}
	p1 := solve1(rows, cols, hash)
	p2 := solve2(rows, cols, hash)
	fmt.Printf("[Part1] : %d\n", p1)
	fmt.Printf("[Part2] : %d\n", p2)
}
