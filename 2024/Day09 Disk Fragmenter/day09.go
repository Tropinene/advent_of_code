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

type blockInfo struct {
	id, start, len int
}

func solve2(s string) int {
	flag, idx := 0, 0
	var blocks []blockInfo
	for i, c := range s {
		l := int(c - '0')
		if i%2 == 0 {
			blocks = append(blocks, blockInfo{flag, idx, l})
			idx += l
			flag += 1
		} else {
			blocks = append(blocks, blockInfo{-1, idx, l})
			idx += l
		}
	}

	for i := len(blocks) - 1; i >= 0; i-- {
		if blocks[i].id < 0 {
			continue
		}

		fileLen := blocks[i].len
		for j := 0; j < i; j++ {
			if blocks[j].id == -1 && blocks[j].len >= fileLen {
				tmp := blockInfo{blocks[i].id, blocks[j].start, fileLen}
				if blocks[j].len > tmp.len {
					newSpace := blockInfo{-1, blocks[j].start + fileLen, blocks[j].len - fileLen}
					blocks[j] = tmp
					blocks[i].id = -2
					blocks = append(blocks[:j+1], append([]blockInfo{newSpace}, blocks[j+1:]...)...)
				} else {
					blocks[j] = tmp
					blocks[i].id = -2
				}
				break
			}
		}
	}

	checksum := 0
	pos := 0
	for _, block := range blocks {
		if block.id >= 0 {
			for k := 0; k < block.len; k++ {
				checksum += pos * block.id
				pos++
			}
		} else {
			pos += block.len
		}
	}

	return checksum
}

//func printBlocks(blocks []blockInfo) {
//	res := ""
//	for _, block := range blocks {
//		if block.id == -1 || block.id == -2 {
//			res += strings.Repeat(".", block.len)
//		} else {
//			res += strings.Repeat(strconv.Itoa(block.id), block.len)
//		}
//	}
//	fmt.Println(res)
//}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))

	p1 := solve1(lines[0])
	fmt.Println("[Part 1]:", p1)
	p2 := solve2(lines[0])
	fmt.Println("[Part 2]:", p2)
}
