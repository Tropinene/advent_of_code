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

func extractNumbers(s string) [2]int {
	var numbers [2]int
	var currentNum, index int
	var hasNum bool

	for _, c := range s {
		if c >= '0' && c <= '9' {
			currentNum = currentNum*10 + int(c-'0')
			hasNum = true
		} else {
			if hasNum {
				numbers[index] = currentNum
				index++
				currentNum = 0
				hasNum = false
			}
		}
	}

	if hasNum {
		numbers[index] = currentNum
	}

	return numbers
}

func solve1(buttonA, buttonB, Prize [2]int) int {
	type State struct {
		x, y   int
		cost   int
		countA int
		countB int
	}

	seen := make(map[[2]int]bool)
	queue := []State{{0, 0, 0, 0, 0}}

	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]

		pos := [2]int{curr.x, curr.y}
		if pos == Prize {
			return curr.cost
		}

		if curr.countA < 100 {
			newX := curr.x + buttonA[0]
			newY := curr.y + buttonA[1]
			newPos := [2]int{newX, newY}
			if !seen[newPos] {
				seen[newPos] = true
				queue = append(queue, State{newX, newY, curr.cost + 3, curr.countA + 1, curr.countB})
			}
		}

		if curr.countB < 100 {
			newX := curr.x + buttonB[0]
			newY := curr.y + buttonB[1]
			newPos := [2]int{newX, newY}
			if !seen[newPos] {
				seen[newPos] = true
				queue = append(queue, State{newX, newY, curr.cost + 1, curr.countA, curr.countB + 1})
			}
		}
	}

	return 0
}

func solve2(buttonA, buttonB, Prize [2]int) int {
	targetX := int64(Prize[0] + 10000000000000)
	targetY := int64(Prize[1] + 10000000000000)

	a := int64(buttonA[0])
	b := int64(buttonB[0])
	c := targetX

	d := int64(buttonA[1])
	e := int64(buttonB[1])
	f := targetY

	det := a*e - b*d
	if det == 0 {
		return 0
	}

	x := (e*c - b*f) / det
	y := (a*f - d*c) / det

	if x*det != (e*c-b*f) || y*det != (a*f-d*c) {
		return 0
	}

	return int(x*3 + y)
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	prizes := readFile(filepath.Join(dir, "input.txt"))
	p1, p2 := 0, 0
	for _, prize := range prizes {
		lines := strings.Split(prize, "\n")
		A, B, P := extractNumbers(lines[0]), extractNumbers(lines[1]), extractNumbers(lines[2])
		p1 += solve1(A, B, P)
		p2 += solve2(A, B, P)
	}
	fmt.Println("[Part 1] : ", p1)
	fmt.Println("[Part 2] : ", p2)
}
