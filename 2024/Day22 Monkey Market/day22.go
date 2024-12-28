package main

import (
	"fmt"
	"math"
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

func hash(num int) int {
	num = ((num << 6) ^ num) & 0xFFFFFF
	num = ((num >> 5) ^ num) & 0xFFFFFF
	num = ((num << 11) ^ num) & 0xFFFFFF
	return num
}

func solve1(secrets []string) int {
	ans := 0
	for _, secret := range secrets {
		num, _ := strconv.Atoi(secret)
		for i := 0; i < 2000; i++ {
			num = hash(num)
		}
		ans += num
	}
	return ans
}

func extractSequences(secret int) map[[4]int]int {
	var res = make(map[[4]int]int)
	var diff []int

	for i := 0; i < 2000; i++ {
		var newSecret = hash(secret)
		diff = append(diff, (newSecret%10)-(secret%10))
		if len(diff) > 4 {
			diff = diff[1:]
		}
		if len(diff) == 4 {
			key := [4]int{diff[0], diff[1], diff[2], diff[3]}
			if _, exists := res[key]; !exists {
				res[key] = newSecret % 10
			}
		}
		secret = newSecret
	}
	return res
}

func solve2(secrets []string) int {
	var sequences = make(map[[4]int]int)
	for _, secret := range secrets {
		num, _ := strconv.Atoi(secret)
		for seq, price := range extractSequences(num) {
			sequences[seq] += price
		}
	}
	var res = math.MinInt
	for _, v := range sequences {
		if v > res {
			res = v
		}
	}
	return res
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
