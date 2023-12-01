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
		linesCh  chan string
		// chunksCh chan string
		// okCh chan bool
		filePath string
		// line     string
		err      error
	)

	// Ingest command line args.
	filePath, err = checkArgs(os.Args)
	checkErr(err)

	// Attempt to open file.
	f, err := os.Open(filePath)
	checkErr(err)
	defer f.Close()

	linesCh = make(chan string)
	// okCh = make(chan bool)
	go FutureScans(f, linesCh)


}

// Change this from 4 to 14 for parts 1 and 2.
const StepSize = 4


func FutureScans(fileObj *os.File, outCh chan<- string) {
	scanner = bufio.NewScanner(fileObj)
	for scanner.Scan() {
		outCh <- scanner.Text()
	}
	return
}

func chunks(data string, size int, chunkSize int, outCh chan<- string) {
	defer close(outCh)
	for i := 0; i < size-chunkSize+1; i++ {
		outCh <- string(data[i : i+chunkSize])
	}
}

func allDistinct(inCh <-chan string, outCh chan<- bool) {
	var cnt int
	var m map[rune]struct{}
	for {
		m = make(map[rune]struct{}, StepSize)
		cnt = 0
		s := <- inCh
		for _, el := range s {
			if _, ok := m[el]; !ok {
				cnt++
			}
		}
		outCh <- cnt == StepSize
	}
}

func checkErr(e error) {
	if e != nil {
		log.Fatal(e)
	}
}


// Change this from 4 to 14 for parts 1 and 2.
// const StepSize = 14

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
