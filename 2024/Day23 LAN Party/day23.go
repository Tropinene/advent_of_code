package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"sort"
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

func checkIfIn(target string, lst []string) bool {
	for _, s := range lst {
		if s == target {
			return true
		}
	}
	return false
}

func findTriplets(hash map[string][]string) int {
	result := 0
	nodes := make([]string, 0)
	for node := range hash {
		nodes = append(nodes, node)
	}

	for i := 0; i < len(nodes); i++ {
		for j := i + 1; j < len(nodes); j++ {
			if !checkIfIn(nodes[j], hash[nodes[i]]) {
				continue
			}

			for k := j + 1; k < len(nodes); k++ {
				if checkIfIn(nodes[k], hash[nodes[i]]) && checkIfIn(nodes[k], hash[nodes[j]]) {
					if strings.HasPrefix(nodes[i], "t") ||
						strings.HasPrefix(nodes[j], "t") ||
						strings.HasPrefix(nodes[k], "t") {
						result += 1
					}
				}
			}
		}
	}
	return result
}

func solve1(lines []string) int {
	hash := make(map[string][]string)
	for _, line := range lines {
		lst := strings.Split(line, "-")
		if _, ok := hash[lst[0]]; !ok {
			hash[lst[0]] = []string{lst[1]}
		} else {
			hash[lst[0]] = append(hash[lst[0]], lst[1])
		}

		if _, ok := hash[lst[1]]; !ok {
			hash[lst[1]] = []string{lst[0]}
		} else {
			hash[lst[1]] = append(hash[lst[1]], lst[0])
		}
	}
	return findTriplets(hash)
}

func findMaxClique(hash map[string][]string) []string {
	nodes := make([]string, 0)
	for node := range hash {
		nodes = append(nodes, node)
	}

	//for size := len(nodes); size >= 1; size-- {
	for size := 13; size >= 1; size-- {
		result := findCliqueSizeK(hash, nodes, size)
		if len(result) > 0 {
			return result
		}
	}
	return []string{}
}

func isValidClique(hash map[string][]string, group []string) bool {
	for i := 0; i < len(group); i++ {
		for j := i + 1; j < len(group); j++ {
			if !checkIfIn(group[j], hash[group[i]]) {
				return false
			}
		}
	}
	return true
}

func findCliqueSizeK(hash map[string][]string, nodes []string, k int) []string {
	var result []string
	var backtrack func(start int, current []string)

	backtrack = func(start int, current []string) {
		if len(result) > 0 {
			return
		}

		if len(current) == k {
			if isValidClique(hash, current) {
				result = append(result, current...)
			}
			return
		}

		if len(current)+(len(nodes)-start) < k {
			return
		}

		for i := start; i < len(nodes); i++ {
			isValid := true
			for _, node := range current {
				if !checkIfIn(nodes[i], hash[node]) {
					isValid = false
					break
				}
			}

			if isValid {
				newCurrent := append([]string{}, current...)
				newCurrent = append(newCurrent, nodes[i])
				backtrack(i+1, newCurrent)
			}
		}
	}

	backtrack(0, []string{})
	return result
}

func solve2(lines []string) string {
	hash := make(map[string][]string)
	for _, line := range lines {
		lst := strings.Split(line, "-")
		if _, ok := hash[lst[0]]; !ok {
			hash[lst[0]] = []string{lst[1]}
		} else {
			hash[lst[0]] = append(hash[lst[0]], lst[1])
		}

		if _, ok := hash[lst[1]]; !ok {
			hash[lst[1]] = []string{lst[0]}
		} else {
			hash[lst[1]] = append(hash[lst[1]], lst[0])
		}
	}

	result := findMaxClique(hash)
	sort.Sort(sort.StringSlice(result))
	return strings.Join(result, ",")
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
