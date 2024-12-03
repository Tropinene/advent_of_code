package main

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
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

	lines := strings.Split(string(data), "\n")
	return lines
}

func scan(s string) int {
	re := regexp.MustCompile(`mul\(\d+,\d+\)`)
	matches := re.FindAllString(s, -1)

	ans := 0
	for _, m := range matches {
		re = regexp.MustCompile(`mul\((\d+),(\d+)\)`)
		lst := re.FindStringSubmatch(m)
		a, _ := strconv.Atoi(lst[1])
		b, _ := strconv.Atoi(lst[2])

		ans += a * b
	}
	return ans
}

func scan2(s string) int {
	re := regexp.MustCompile(`mul\(\d+,\d+\)|don't\(\)|do\(\)`)
	matches := re.FindAllString(s, -1)
	//fmt.Println(matches)
	ans := 0
	isDisabled := false
	for _, m := range matches {
		if m[0:3] == "mul" {
			if isDisabled {
				continue
			}
			re = regexp.MustCompile(`mul\((\d+),(\d+)\)`)
			lst := re.FindStringSubmatch(m)
			a, _ := strconv.Atoi(lst[1])
			b, _ := strconv.Atoi(lst[2])
			ans += a * b
		} else if m[0:3] == "don" {
			isDisabled = true
		} else {
			isDisabled = false
		}
	}
	return ans
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))
	p1, p2 := 0, 0
	s := ""
	for _, line := range lines {
		s += line
	}
	p1 = scan(s)
	p2 = scan2(s)
	fmt.Printf("[Part 1]: %d\n", p1)
	fmt.Printf("[Part 2]: %d\n", p2)
}
