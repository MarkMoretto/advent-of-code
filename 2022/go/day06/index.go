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

/*
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
*/
