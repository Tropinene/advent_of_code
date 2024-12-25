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
	return strings.Split(strings.TrimSpace(string(data)), "\n\n")
}

func initGraphs(graphs []string) ([][]int, [][]int) {
	var keys, locks [][]int
	for _, graph := range graphs {
		glst := strings.Split(graph, "\n")
		if glst[0] == "#####" {
			lock := []int{0, 0, 0, 0, 0}
			for i := 1; i < len(glst)-1; i++ {
				for j := 0; j < len(glst[i]); j++ {
					if glst[i][j] == '#' {
						lock[j]++
					}
				}
			}
			locks = append(locks, lock)
		} else {
			key := []int{0, 0, 0, 0, 0}
			for i := 1; i < len(glst)-1; i++ {
				for j := 0; j < len(glst[i]); j++ {
					if glst[i][j] == '#' {
						key[j]++
					}
				}
			}
			keys = append(keys, key)
		}
	}
	return keys, locks
}

func solve1(keys, locks [][]int) int {
	res := 0
	for _, key := range keys {
		for _, lock := range locks {
			flag := true
			for i := 0; i < 5; i++ {
				if key[i]+lock[i] > 5 {
					flag = false
					break
				}
			}
			if flag {
				res++
			}
		}
	}

	return res
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	graphs := readFile(filepath.Join(dir, "input.txt"))

	keys, locks := initGraphs(graphs)
	p1 := solve1(keys, locks)
	fmt.Println("[Part 1]:", p1)

}
