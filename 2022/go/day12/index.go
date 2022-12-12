package main

// https://adventofcode.com/2022/day/12

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

}

// Main solution.
func solve(f *os.File) {
	defer f.Close()

	var (
		line string
		g Grid
		rc RowCol
		sPt, ePt *point
	)
	g = newGrid()

	scanner = bufio.NewScanner(f)
	for scanner.Scan() {
		line = scanner.Text()
		rc = newRowCol()
		for _, chr := range line {
			rc = append(rc, chr)
		}
		g = append(g, rc)
	}

	for r := range g {
		for c, chr := range g[r] {
			rc = g[r]
			switch chr {
				case 'S':
				sPt = newPoint(r, c)
				rc[c] = 0
				g[r] = rc
				printf("Start: (%d, %d)\n", sPt.r, sPt.c)
				case 'E':
				ePt = newPoint(r, c)
				rc[c] = 99
				g[r] = rc				
				printf("End: (%d, %d)\n", ePt.r, ePt.c)
			}
		}
		// printf("%v\n", g[i])
	}
}

type point struct {
	r, c int
}

func newPoint(a, b int) *point {
	return &point{a, b}
}


const MaxWidthHeight = 50

type RowCol []rune
type Grid []RowCol

func newRowCol() RowCol {
	out := make(RowCol, 0, MaxWidthHeight)
	return out
}

func newGrid() Grid {
	out := make(Grid, 0, MaxWidthHeight)
	for range out {
		out = append(out, newRowCol())
	}
	return out
}


var scanner *bufio.Scanner
var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanws(a ...interface{}) { fmt.Fscan(reader, a...) }
