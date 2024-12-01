package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"runtime"
	"sort"
	"strconv"
	"strings"
)

func readNumbers(filename string) ([]int, []int, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, nil, err
	}
	defer file.Close()

	var nums1, nums2 []int
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		if len(fields) >= 2 {
			num1, err := strconv.Atoi(fields[0])
			if err != nil {
				return nil, nil, err
			}
			num2, err := strconv.Atoi(fields[1])
			if err != nil {
				return nil, nil, err
			}

			nums1 = append(nums1, num1)
			nums2 = append(nums2, num2)
		}
	}

	if err := scanner.Err(); err != nil {
		return nil, nil, err
	}

	return nums1, nums2, nil
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func solve1(nums1 []int, nums2 []int) int {
	ans := 0
	l := len(nums1)
	for i := 0; i < l; i++ {
		ans += abs(nums1[i] - nums2[i])
	}
	return ans
}

func solve2(nums1 []int, nums2 []int) int {
	hash := make(map[int]int)
	for _, num := range nums2 {
		hash[num]++
	}
	ans := 0
	for _, num := range nums1 {
		if hash[num] > 0 {
			ans += hash[num] * num
		}
	}
	return ans
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	nums1, nums2, err := readNumbers(dir + "/input.txt")
	if err != nil {
		log.Fatal(err)
		return
	}
	p2 := solve2(nums1, nums2)
	sort.Ints(nums1)
	sort.Ints(nums2)
	p1 := solve1(nums1, nums2)
	fmt.Printf("[Part1]: %d\n", p1)
	fmt.Printf("[Part2]: %d\n", p2)
}
