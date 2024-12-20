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

	lines := strings.Split(string(data), "\n\n")
	return lines
}

func createRules(lines []string) map[string][]string {
	hash := make(map[string][]string)
	for _, line := range lines {
		tmp := strings.Split(line, "|")
		a, b := tmp[0], tmp[1]
		if _, ok := hash[a]; !ok {
			hash[a] = []string{b}
		} else {
			hash[a] = append(hash[a], b)
		}
	}
	return hash
}

func checkItem(hash map[string][]string, a string, b string) bool {
	if _, ok := hash[a]; !ok {
		return true
	}
	lst := hash[a]
	for _, v := range lst {
		if v == b {
			return false
		}
	}
	return true
}

func checkLine(hash map[string][]string, lst []string) bool {
	for i := len(lst) - 1; i >= 0; i-- {
		for j := i - 1; j >= 0; j-- {
			if checkItem(hash, lst[i], lst[j]) == false {
				return false
			}
		}
	}
	return true
}

func correctLst(hash map[string][]string, lst []string) int {
	for i := len(lst) - 1; i >= 0; i-- {
		for j := i - 1; j >= 0; j-- {
			if checkItem(hash, lst[i], lst[j]) == false {
				var newLst []string
				newLst = append(newLst, lst[:j]...)
				newLst = append(newLst, lst[j+1:i+1]...)
				newLst = append(newLst, lst[j])
				newLst = append(newLst, lst[i+1:]...)
				for checkLine(hash, newLst) == false {
					return correctLst(hash, newLst)
				}
				res, _ := strconv.Atoi(newLst[len(newLst)/2])
				return res
			}
		}
	}
	return 0
}

func solve1(rules, update []string) int {
	hash := createRules(rules)
	res := 0
	for _, line := range update {
		lst := strings.Split(line, ",")
		if checkLine(hash, lst) {
			mid, _ := strconv.Atoi(lst[len(lst)/2])
			res += mid
		}
	}
	return res
}

func solve2(rules, update []string) int {
	hash := createRules(rules)
	res := 0
	for _, line := range update {
		lst := strings.Split(line, ",")
		if !checkLine(hash, lst) {
			mid := correctLst(hash, lst)
			res += mid
		}
	}
	return res
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	parts := readFile(filepath.Join(dir, "input.txt"))
	rules, update := parts[0], parts[1]

	p1 := solve1(strings.Split(rules, "\n"), strings.Split(update, "\n"))
	fmt.Printf("[Part 1]: %d\n", p1)
	p2 := solve2(strings.Split(rules, "\n"), strings.Split(update, "\n"))
	fmt.Printf("[Part 2]: %d\n", p2)
}
