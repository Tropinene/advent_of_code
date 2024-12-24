package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: go run main.go <day-number>")
		return
	}

	// Parse day number
	num, err := strconv.Atoi(os.Args[1])
	if err != nil || num < 1 || num > 25 {
		fmt.Println("Please provide a valid day number between 1 and 25")
		return
	}

	// Fetch the webpage
	url := fmt.Sprintf("https://adventofcode.com/2024/day/%d", num)
	resp, err := http.Get(url)
	if err != nil {
		fmt.Printf("Error fetching webpage: %v\n", err)
		return
	}
	defer func(Body io.ReadCloser) {
		err := Body.Close()
		if err != nil {

		}
	}(resp.Body)

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Extract target using regex
	re := regexp.MustCompile(`<h2>--- (Day \d+: .+?) ---</h2>`)
	matches := re.FindStringSubmatch(string(body))
	if len(matches) < 2 {
		fmt.Println("Could not find the title in the webpage")
		return
	}

	// Format the title
	title := matches[1]
	dayNum := fmt.Sprintf("%02d", num)
	title = strings.Replace(title, fmt.Sprintf("Day %d", num), fmt.Sprintf("Day%s", dayNum), 1)
	title = strings.Replace(title, ":", "", -1)

	// Create directory
	err = os.MkdirAll(filepath.Join("..", title), 0755)
	if err != nil {
		fmt.Printf("Error creating directory: %v\n", err)
		return
	}

	// Create input.txt
	inputPath := filepath.Join("..", title, "input.txt")
	err = os.WriteFile(inputPath, []byte(""), 0644)
	if err != nil {
		fmt.Printf("Error creating input.txt: %v\n", err)
		return
	}

	// Create Go file
	goContent := `package main

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
    return strings.Split(strings.TrimSpace(string(data)), "\n")
}

func main() {
    _, filename, _, _ := runtime.Caller(0)
    dir := filepath.Dir(filename)
    lines := readFile(filepath.Join(dir, "input.txt"))

}`

	goFileName := fmt.Sprintf("day%s.go", dayNum)
	goPath := filepath.Join("..", title, goFileName)
	err = os.WriteFile(goPath, []byte(goContent), 0644)
	if err != nil {
		fmt.Printf("Error creating %s: %v\n", goFileName, err)
		return
	}

	fmt.Printf("Successfully created:\n- Directory: %s\n- Files: input.txt and %s\n", title, goFileName)
}
