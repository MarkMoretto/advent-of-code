package main

// https://adventofcode.com/2022/day/23

import (
	"bufio"
	_ "bytes"
	"fmt"
	"log"
	"os"
	_ "strings"
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

// Main solver function.
func solve(f *os.File) {
	defer f.Close()
	var (
		line string
		rowNum int
	)

	elves := make(Elves, 0, 1e4)

	scanner = bufio.NewScanner(f)
	for scanner.Scan() {
		line = scanner.Text()
		for c, el := range line {
			if el == '#' {
				elves = append(elves, &point{rowNum, c})
			}
		}
		rowNum++
		printf("%s\n", line)
	}

}

// https://github.com/codertee/adventofcode/blob/466aaffb219b9aab299d65c8e825d9ecf9f5b850/adventofcode/solutions/y2022/d23.py

type point struct {
	row, col int
}

func (p *point) EqualTo(other *point) bool {
	return p.row == other.row && p.col == other.col
}

func EqualTo(p1, p2 *point) bool {
	return p1.row == p2.row && p1.col == p2.col
}

func (p *point) newDir(d *point) *point {
	return &point{p.row+d.row, p.col+d.col}
}

type DirAbbr string
type DirectionMap map[DirAbbr]*point

func directions() *DirectionMap {
	return &DirectionMap{
		"N":  {-1, 0},
		"S":  {1, 0},
		"W":  {0, -1},
		"E":  {1, 0},
		"NE": {-1, 1},
		"NW": {-1, -1},
		"SE": {1, 1},
		"SW": {1, -1},
	}
}

func getDirection(abbr DirAbbr) *point {
	if pt, ok := (*directions())[abbr]; ok {
		return pt
	}
	return nil
}

// Number of subgroups.
const nSubGroups = 4

// Return direction groups.
func directionGroups() [][]DirAbbr {
	return [][]DirAbbr{
		{"N", "NE", "NW"},
		{"S", "SE", "SW"},
		{"W", "NW", "SW"},
		{"E", "NE", "SE"},
	}
}

// Retrieve subgroup based on index value.
func directionGroup(dirKey int) []DirAbbr {
	return directionGroups()[dirKey]
}

// Elf group struct.
type Elves []*point

// Check if proposed elf within elves.
func (e *Elves) Contains(proposedElf *point) bool {
	for _, elf := range *e {
		if elf.EqualTo(proposedElf) {
			return true
		}
	}
	return false
}

// Look in all eight directions to see if another elf
// already occupying space.
func (e *Elves) LookArounOkay(elf *point) bool {
	var testPt *point
	for _, pt := range *directions() {
		testPt = elf.newDir(pt)
		if e.Contains(testPt) {
			return false
		}
	}
	return true
}

// Based on current group of elves, check the sub-group of points in each
// direction for a given elf and, if no current elf is in one of those
// points, return true.
func (e *Elves) checkSubGroup(nextPt *point, dirs []DirAbbr) bool {
	var testPt *point
	for _, d := range dirs {
		testPt = nextPt.newDir(getDirection(d))
		if e.Contains(testPt) {
			return false
		}
	}
	return true
}

// Run first and second half of checks.
func sim(e *Elves) {
	// var nextPt *point
	// var proposedMoves Elves
	var dirGroup []DirAbbr
	var nextMove DirAbbr
	var moveMap map[DirAbbr][]*point
	var nRounds int
	var startIndex, subIndex int
	moveMap = map[DirAbbr][]*point{}
	// moveMap["N"] = []*point{}
	// moveMap["S"] = []*point{}
	// moveMap["W"] = []*point{}
	// moveMap["E"] = []*point{}
	for _, elf := range *e {
		// Check all directions.  If no other elf found,
		// move on to the next elf.
		if e.LookArounOkay(elf) {
			continue
		}

		subIndex = startIndex
		for i := 0; i < 4; i++ {
			dirGroup = directionGroup((subIndex+i)%4)
			nextMove = dirGroup[0]
			if e.checkSubGroup(elf, dirGroup) {
				// This should use a point for key.
				moveMap[nextMove] = append(moveMap[nextMove], elf.newDir(getDirection(nextMove)))
			}
		}
	}

	// for k, v := range moveMap {
	// 	if len(v) == 1 {
	// 		*e = append(*e, )
	// 	}
	// }

	nRounds++
	startIndex = nRounds%4
}

var scanner *bufio.Scanner
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }


// func genDirections() <-chan *point {
// 	outCh := make(chan *point)
// 	go func() {
// 		for r := -1; r < 2; r++ {
// 			for c := -1; c < 2; c++ {
// 				// Don't want Point{0, 0}
// 				if r+c != 0 && r != 0 || c != 0 {
// 					outCh <- &point{r, c}
// 				}
// 			}
// 		}
// 		close(outCh)
// 	}()
// 	return outCh
// }