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

func solve1(secrets []string) int {
	ans := 0
	for _, secret := range secrets {
		num, _ := strconv.Atoi(secret)
		for i := 0; i < 2000; i++ {
			num = ((num << 6) ^ num) & 0xFFFFFF
			num = ((num >> 5) ^ num) & 0xFFFFFF
			num = ((num << 11) ^ num) & 0xFFFFFF
		}
		ans += num
	}
	return ans
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))

	p1 := solve1(lines)
	fmt.Println("[Part 1]:", p1)
}
