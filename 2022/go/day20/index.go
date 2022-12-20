package main

// https://adventofcode.com/2022/day/20

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

const MaxLines = 5_000

// Main solver function.
func solve(f *os.File) {
	defer f.Close()

	var (
		line string
		ints []int
	)
	ints = make([]int, 0, MaxLines)

	scanner = bufio.NewScanner(f)

	for scanner.Scan() {
		line = scanner.Text()
		ints = append(ints, strToAnyInt(line))

		printf("%s\n", line)

	}

}


func strToAnyInt[S string, I int](s S) I {
	const Ten = 10

	var out I
	var isNeg bool

	if s[0] == '-' {
		isNeg = true
		s = s[1:]
	}

	for _, el := range s {
		out *= Ten
		out += I(el - '0')
	}
	if isNeg {
		out = -out
	}
	return out
}


var scanner *bufio.Scanner
var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanws(a ...interface{}) { fmt.Fscan(reader, a...) }
