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

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))

	p1 := solve1(lines)
	fmt.Println("[Part 1]:", p1)
}
