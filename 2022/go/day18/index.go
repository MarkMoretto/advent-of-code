package main

// https://adventofcode.com/2022/day/18

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

const MaxCubes = 3_000

// Main solver.
func solve(f *os.File) {
	defer f.Close()

	var (
		cubes Cubes
		// bCubes BoolCubes
		tmp *pos
		line string
		nPoints int
	)
	cubes = make(Cubes, 0, MaxCubes)
	// bCubes = make(BoolCubes, MaxCubes)

	scanner = bufio.NewScanner(f)
	for scanner.Scan() {
		line = scanner.Text()
		tmp = newPos(line)
		cubes = append(cubes, tmp)
	}


	for i, pt1 := range cubes {
		nPoints += 6
		// printf("%d: %#v\n", i, pt1)
		for _, d := range directions() {
			tmp = pt1.IncrPoint(d)
			for j, pt2 := range cubes {
				if i != j && pt2.EqualTo(tmp) {
					// printf("  %v\n", tmp)
					nPoints--					
				}
			}
		}
	}
	printf("%d\n", nPoints)
}


type pos struct {
	x, y, z int
}

type Cubes []*pos
type BoolCubes map[*pos]bool

func newPos(txt string) *pos {
	tmp := strings.Split(txt, ",")
	return &pos{
		x: strToInt(tmp[0]),
		y: strToInt(tmp[1]),
		z: strToInt(tmp[2]),
	}
}

func (p *pos) EqualTo(other *pos) bool {
	return p.x==other.x && p.y==other.y && p.z==other.z
}

func (p *pos) IncrPoint(direction *pos) *pos {
	return &pos{p.x+direction.x, p.y+direction.y, p.z+direction.z}
}

// Check arond cube
func directions() []*pos {
	return []*pos{
		{ 1, 0, 0},
		{ 0, 1, 0},
		{ 0, 0, 1},
		{-1, 0, 0},
		{ 0,-1, 0},
		{ 0, 0,-1},
	}
}



// Utility
func strToInt(x string) int {
	var out int
	for _, el := range x {
		out = out * 10 + int(el - '0')
	}
	return out
}

var scanner *bufio.Scanner
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
