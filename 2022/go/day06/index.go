package main

// https://adventofcode.com/2022/day/6

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	defer writer.Flush()
	var (
		f *os.File
		dataPath string
		err error
	)

	// Get data path.
	if len(os.Args) > 1 {
		dataPath = os.Args[1]
	}

	// Open file and handle related error, if required.
	f, err = os.Open(dataPath)
	if err != nil {
		log.Fatal(err)
	}

	solve(f)

}

func solve(f *os.File) {
	defer f.Close()
	var line string
	scanner = bufio.NewScanner(f)
	for scanner.Scan() {
		line = scanner.Text()
		printf("%d %s\n", firstNUniqueIndex(line), line)
	}
}

const StepSize = 4
func firstNUniqueIndex(s string) int {
	var i, n int
	var chunk string
	var fMap map[rune]struct{}

	n = len(s)
	for i < n-StepSize+1 {
		fMap = make(map[rune]struct{}, n)
		chunk = s[i : i+StepSize]
		for _, el := range chunk {
			if _, ok := fMap[el]; !ok {
				fMap[el] = struct{}{}
			}
		}
		if len(fMap) == StepSize {
			return i + StepSize
		}
		i++
	}
	return -1
}

var scanner *bufio.Scanner
var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanws(a ...interface{}) { fmt.Fscan(reader, a...) }
