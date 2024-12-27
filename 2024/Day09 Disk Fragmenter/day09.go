package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strconv"
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

func solve1(s string) int {
	var res []int
	flag, ans := 0, 0
	for i, c := range s {
		n, _ := strconv.Atoi(string(c))
		if i%2 == 0 {
			for j := 0; j < n; j++ {
				res = append(res, flag)
			}
			flag += 1
		} else {
			for j := 0; j < n; j++ {
				res = append(res, -1)
			}
		}
	}

	i, j := 0, len(res)-1
	for i != j {
		for i < j && res[i] != -1 {
			i++
		}
		for j > i && res[j] == -1 {
			j--
		}
		res[i], res[j] = res[j], res[i]
	}

	for k := 0; k < len(res); k++ {
		if res[k] == -1 {
			break
		}
		ans += res[k] * k
	}
	return ans
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))

	p1 := solve1(lines[0])
	fmt.Println("[Part 1]:", p1)
}
