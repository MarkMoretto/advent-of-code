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

const MaxNumbers = 7

// Main solver function.
func solve(f *os.File) {
	defer f.Close()

	var (
		line string
		ints []int
		worker []int
		tmp int
	)
	ints = make([]int, 0, MaxNumbers)
	scanner = bufio.NewScanner(f)

	for scanner.Scan() {
		line = scanner.Text()
		tmp = strToAnyInt(line)
		ints = append(ints, tmp)
		worker = append(worker, tmp)
	}

	for i, v := range ints {
		//TODO: Check sign
		//TODO: Rotate worker.
		printf("%d %d\n", i, v)
	}

}


// func rotateCW(a []int, nPlaces int) []int {
// 	for nPlaces > 0 {
//      blank line
// 		nPlaces--
// 	}
// }

func push(a []int, val int) []int {
	a = append(a, val)
	return a
}

func pop(a []int, val int) int {
	var x int
	var n int
	n = len(a)
	x, a = a[n-1], a[:n-1]
	return x
}

func indexOf(a []int, val int) int {
	for i := range a {
		if a[i] == val {
			return i
		}
	}
	return -1
}

func insertAt(a []int, val, idx int) []int {
	a = append(a, 0)
	copy(a[idx+1:], a[idx:])
	a[idx] = val
	return a
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
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
