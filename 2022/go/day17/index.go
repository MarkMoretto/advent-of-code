package main

// https://adventofcode.com/2022/day/17

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

	// Run solution.
	solve(f)

	return
}


// Main solver function.
const (
	Width = 7
	NumRocks = 2022
)

func solve(f *os.File) {
	defer f.Close()

	var (
		line string
		n int
		// nRocks int
		// height int
		// nObjects int
	)
	scanner = bufio.NewScanner(f)
	for scanner.Scan() {
		line = scanner.Text()
	}
	n = len(line)

	printf("%d\n", n)
	printf("%d %d\n", n/NumRocks, n%NumRocks)
}

type shape struct {
	w, h int
}

func shapes() {
	
}












var scanner *bufio.Scanner
var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanws(a ...interface{}) { fmt.Fscan(reader, a...) }
