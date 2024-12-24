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

func myInit(lines []string) (int, int, int, []int) {
	tmp := strings.Split(lines[0], " ")[2]
	A, _ := strconv.Atoi(tmp)

	tmp = strings.Split(lines[1], " ")[2]
	B, _ := strconv.Atoi(tmp)

	tmp = strings.Split(lines[2], " ")[2]
	C, _ := strconv.Atoi(tmp)

	tmp = strings.Split(lines[4], " ")[1]
	programStr := strings.Split(tmp, ",")
	var programs []int
	for _, s := range programStr {
		n, _ := strconv.Atoi(s)
		programs = append(programs, n)
	}
	return A, B, C, programs
}

func getOP(op, A, B, C int) int {
	if op <= 3 {
		return op
	} else if op == 4 {
		return A
	} else if op == 5 {
		return B
	} else if op == 6 {
		return C
	}
	return -1
}

func solve1(A, B, C int, progs []int) string {
	ptr := 0
	l := len(progs)
	var output []string
	for ptr < l {
		ins, op := progs[ptr], progs[ptr+1]
		if ins == 0 {
			A = A / (1 << getOP(op, A, B, C))
		} else if ins == 1 {
			B ^= op
		} else if ins == 2 {
			B = getOP(op, A, B, C) % 8
		} else if ins == 3 {
			if A != 0 {
				//ptr = getOP(op, A, B, C)
				ptr = op
				continue
			}
		} else if ins == 4 {
			B ^= C
		} else if ins == 5 {
			output = append(output, strconv.Itoa(getOP(op, A, B, C)%8))
		} else if ins == 6 {
			B = A / (1 << getOP(op, A, B, C))
		} else if ins == 7 {
			C = A / (1 << getOP(op, A, B, C))
		} else {

		}
		ptr += 2
	}
	return strings.Join(output, ",")
}

func solve2(B, C int, progs []int) string {
	var progStr []string
	for _, p := range progs {
		progStr = append(progStr, strconv.Itoa(p))
	}
	//ans := strings.Join(progStr, ",")
	//s := solve1(A, B, C, progs)

	startA := 216584200000000
	//        216584205979245
	for true {
		A := startA
		matchIdx := 0
		ptr := 0
		l := len(progs)
		var output []string

		for ptr < l {
			ins, op := progs[ptr], progs[ptr+1]
			if ins == 0 {
				A = A / (1 << getOP(op, A, B, C))
			} else if ins == 1 {
				B ^= op
			} else if ins == 2 {
				B = getOP(op, A, B, C) % 8
			} else if ins == 3 {
				if A != 0 {
					ptr = op
					continue
				}
			} else if ins == 4 {
				B ^= C
			} else if ins == 5 {
				tmp := getOP(op, A, B, C) % 8
				if tmp != progs[matchIdx] {
					break
				} else {
					output = append(output, strconv.Itoa(tmp))
					matchIdx++
				}
			} else if ins == 6 {
				B = A / (1 << getOP(op, A, B, C))
			} else if ins == 7 {
				C = A / (1 << getOP(op, A, B, C))
			} else {

			}
			ptr += 2
		}
		if matchIdx == len(progStr) {
			break
		}
		startA++
	}

	return strconv.Itoa(startA)
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))

	A, B, C, programs := myInit(lines)
	p1 := solve1(A, B, C, programs)
	fmt.Println("[Part 1]:", p1)
	p2 := solve2(B, C, programs)
	fmt.Println("[Part 2]:", p2)
}
