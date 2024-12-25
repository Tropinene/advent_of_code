package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"sort"
	"strconv"
	"strings"
)

type signal struct {
	device1 string
	device2 string
	logic   string
	storage string
}

func readFile(fileName string) []string {
	data, err := os.ReadFile(fileName)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return []string{}
	}
	return strings.Split(strings.TrimSpace(string(data)), "\n\n")
}

func initInput(input []string) map[string]int {
	hash := make(map[string]int)
	for _, v := range input {
		lst := strings.Split(v, ": ")
		gate := lst[0]
		value, _ := strconv.Atoi(lst[1])
		hash[gate] = value
	}
	return hash
}

func initConnections(connections []string) []signal {
	var signals []signal
	for _, v := range connections {
		lst := strings.Split(v, " ")
		tmp := signal{device1: lst[0], device2: lst[2], logic: lst[1], storage: lst[4]}
		signals = append(signals, tmp)
	}
	return signals
}

func initGates(input map[string]int, connections []signal) map[string]int {
	res := make(map[string]int)
	for k, v := range input {
		res[k] = v
	}

	for _, v := range connections {
		if _, ok := res[v.device1]; !ok {
			res[v.device1] = -1
		}
		if _, ok := res[v.device2]; !ok {
			res[v.device2] = -1
		}
		if _, ok := res[v.storage]; !ok {
			res[v.storage] = -1
		}
	}

	return res
}

func solve1(connections []signal, gates map[string]int) int {
	for i := 0; i < len(connections); i++ {
		for _, v := range connections {
			if gates[v.device1] != -1 && gates[v.device2] != -1 {
				switch v.logic {
				case "AND":
					gates[v.storage] = gates[v.device1] & gates[v.device2]
				case "OR":
					gates[v.storage] = gates[v.device1] | gates[v.device2]
				case "XOR":
					gates[v.storage] = gates[v.device1] ^ gates[v.device2]
				}
			}
		}
	}

	zGates := make(map[string]int)
	var keys []string
	for k, v := range gates {
		if k[0] == 'z' {
			zGates[k] = v
			keys = append(keys, k)
		}
	}
	sort.Strings(keys)
	resStr := ""
	for i := len(keys) - 1; i >= 0; i-- {
		resStr += strconv.Itoa(zGates[keys[i]])
		//fmt.Println(keys[i], zGates[keys[i]])
	}
	ans, _ := strconv.ParseInt(resStr, 2, 64)

	return int(ans)
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	lines := readFile(filepath.Join(dir, "input.txt"))
	input := initInput(strings.Split(lines[0], "\n"))
	connections := initConnections(strings.Split(lines[1], "\n"))
	gates := initGates(input, connections)

	p1 := solve1(connections, gates)
	fmt.Println("[Part 1]:", p1)
}
