package main

// https://adventofcode.com/2022/day/5

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strings"
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
	
	// Run solutions
	solve(f)
	// printf("%d\n", res)
}

// Solution.
const SplitPattern = `\s+`
const ScanPattern = `move %d from %d to %d`

func solve(f *os.File) {
	defer f.Close()

	var (
		r *regexp.Regexp
		parts []string
		allParts [][]string
		stacks []*stack
		line string
		err error
		nMoves, fromIdx, toIdx int
	)

	allParts = [][]string{}
	stacks = make([]*stack, 0, 1000)

	// Init regex object.
	r = regexp.MustCompile(SplitPattern)

	scanner = bufio.NewScanner(f)

	for scanner.Scan() {
		line = scanner.Text()
		if len(line) == 0 {
			// Make stacks
			for i := range allParts {
				stk := newStack()
				for j, el := range allParts[i] {
					if len(el) > 0 {
						fmt.Println(i, j, el)
						stk.Push(el)
					}
				}
				stacks = append(stacks, stk)
			}
			continue
		}

		if strings.Contains(line, "[") {
			parts = r.Split(line, -1)
			allParts = append(allParts, parts)
		} else {
			_, err := fmt.Sscanf(line, ScanPattern, &nMoves, &fromIdx, &toIdx)
			if err != nil {
				panic(err)
			}
			fromIdx--
			toIdx--
			for nMoves > 0 {
				tmp:=stacks[fromIdx].Pop()
				stacks[toIdx].Push(tmp)
				nMoves--
			}
		}
	}

	if err = scanner.Err(); err != nil {
        log.Fatal(err)
    }

	// Return.
	printf("%v\n", stacks)
}

type stack []string

func newStack() *stack {
	return &stack{}
}

func (s *stack) Len() int { return len(*s) }

func (s *stack) Push(v string) {
	*s = append(*s, v)
}

func (s *stack) Pop() string {
	var out string
	out, *s = (*s)[s.Len()-1], (*s)[:s.Len()-1]
	return out
}

// Common functions.

// Convenience function to split by comma.
func splitComma(s string) []string {
	return strings.Split(s, ",")
}

// Convert string to integer.
// Note: This is quicker than `strconv.Atoi()`.
func stringToInt(s string) int {
	var out int
	b := []byte(s)
	for _, el := range b {
		out = out*10 + int(el-'0')
	}
	return out
}


var scanner *bufio.Scanner
var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanws(a ...interface{}) { fmt.Fscan(reader, a...) }
