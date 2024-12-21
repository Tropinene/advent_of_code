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

func solve1(nums []string, round int) int {
	for round > 0 {
		var nextNums []string
		for _, n := range nums {
			if n == "0" {
				nextNums = append(nextNums, "1")
			} else if len(n)%2 == 0 {
				mid := len(n) / 2
				nextNums = append(nextNums, n[:mid])
				tmp := n[mid:]
				for tmp[0] == '0' && len(tmp) > 1 {
					tmp = tmp[1:]
				}
				if len(tmp) == 0 {
					nextNums = append(nextNums, "0")
				} else {
					nextNums = append(nextNums, tmp)
				}
			} else {
				tmp, _ := strconv.Atoi(n)
				tmp *= 2024
				nextNums = append(nextNums, strconv.Itoa(tmp))
			}
		}
		//fmt.Println(nextNums)
		nums = nextNums
		round -= 1
	}
	return len(nums)
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))

	numsStr := strings.Split(lines[0], " ")
	p1 := solve1(numsStr, 25)
	fmt.Printf("[Part1] : %d\n", p1)
}
