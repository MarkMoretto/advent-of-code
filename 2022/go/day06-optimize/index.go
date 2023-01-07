package main

// https://adventofcode.com/2022/day/6

// See: https://f4t.dev/software/go-performance-memory/

// Test data: https://raw.githubusercontent.com/busser/adventofcode/main/y2022/d06/testdata/input.txt

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	defer writer.Flush()
	var (
		filePath string
		line     string
		err      error
	)

	// Ingest command line args.
	filePath, err = checkArgs(os.Args)
	if err != nil {
		log.Fatal(err)
	}

	// Attempt to open file.
	f, err := os.Open(filePath)
	if err != nil {
		log.Fatal(err)
	}

	// Scan each line of file and process as required.
	scanner = bufio.NewScanner(f)
	for scanner.Scan() {
		line = scanner.Text()
		solution(line, len(line))
	}
}

// Change this from 4 to 14 for parts 1 and 2.
const StepSize = 14

func solution(s string, sz int) {
	var i int
	var tmp string
	for i = 0; i < sz; i++ {
		tmp = s[i : i+StepSize]
		if nUnique(tmp) == StepSize {
			fmt.Printf("%d\n", i+StepSize)
			return
		}
	}
	fmt.Printf("Solution not found!\n")
}

// Number of unique characters
func nUnique(ss string) int {
	bMap := make(map[rune]struct{}, len(ss))
	for _, chr := range ss {
		if _, ok := bMap[chr]; !ok {
			bMap[chr] = struct{}{}
		}
	}
	return len(bMap)
}

// Check command-line args.
func checkArgs(args []string) (string, error) {
	n := len(args)
	if n != 2 {
		return "", fmt.Errorf("Too few arguments passed to program. Expected 2, got %d.", n)
	}
	return args[1], nil
}

var scanner *bufio.Scanner
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(frmt string, a ...interface{}) { fmt.Fprintf(writer, frmt, a...) }
