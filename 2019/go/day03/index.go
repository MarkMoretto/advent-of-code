package main

// https://adventofcode.com/2019/day/3

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	defer writer.Flush()

	var (
		f             *os.File
		currPt        *Point
		dataPath, txt string
		direction     string
		amount        int
		err           error
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

	scanner = bufio.NewScanner(f)
	for scanner.Scan() {
		txt = scanner.Text()
		currPt = getOrigin()
		for _, pair := range strings.Split(txt, ",") {
			direction, amount = getDirAmt(pair)
			Move(currPt, getDirectionPoint(direction), amount)
			printf("%s\n", currPt)
		}
	}

	if err = scanner.Err(); err != nil {
		log.Fatal(err)
	}

	if err = f.Close(); err != nil {
		log.Fatal(err)
	}

	// part 1

	// part 2

}

// Part 1 solution

func part1(f *os.File) int {
	defer f.Close()
	return 1
}

// Part 2 solution

func part2(f *os.File) int {
	defer f.Close()
	return 1
}

type Point [2]int

func (p *Point) String() string {
	return fmt.Sprintf("(%d, %d)", p[0], p[1])
}

func newPoint(x, y int) *Point {
	return &Point{x, y}
}

func getOrigin() *Point {
	return newPoint(0, 0)
}

func Move(pt, dir *Point, magnitude int) {
	(*pt)[0] += ((*dir)[0] * magnitude)
	(*pt)[1] += ((*dir)[1] * magnitude)
}

// Direction points.
func getDirectionPoint(direction string) *Point {
	switch direction {
	case "U":
		return newPoint(0, 1)
	case "D":
		return newPoint(0, -1)
	case "L":
		return newPoint(-1, 0)
	case "R":
		return newPoint(1, 0)
	default:
		return nil
	}
}

// Functions.
func getDirAmt(s string) (string, int) {
	return s[:1], stringToInt(s[1:])
}

func stringToInt(s string) int {
	var out int
	b := []byte(s)
	for _, el := range b {
		out = out*10 + int(el-'0')
	}
	return out
}

func DemoProcess(s string) {
	var direction byte
	var amount string
	wirePaths := []string{
		"R8,U5,L5,D3",
		"U7,R6,D4,L4",
	}
	for _, path := range wirePaths {
		for _, pair := range strings.Split(path, ",") {
			direction, amount = pair[0], pair[1:]
			fmt.Println(string(direction), amount)
		}
	}
}

var scanner *bufio.Scanner
var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanws(a ...interface{})           { fmt.Fscan(reader, a...) }
