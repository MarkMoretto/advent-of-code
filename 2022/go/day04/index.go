package main

// https://adventofcode.com/2022/day/4

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
		res int
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
	
	// Parts 1 and 2.
	res = solve(f)
	printf("%d\n", res)
}

// Info. that is provided in the problem statement.
const ElfCount = 2

// Solution.
func solve(f *os.File) int {
	defer f.Close()
	var (
		elves []*pair
		txt string
		err error
		subsetCount int
	)

	scanner = bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		txt = scanner.Text()
		
		// Create slice of pairs for each assignment range.
		elves = make([]*pair, ElfCount)

		// Split assignment range and assign to each elf.
		for elfId, section := range splitComma(txt) {
			elves[elfId] = getPair(section)
		}

		// Part 1 solution

		// // Count full range subsets.
		// switch {
		// case elves[0].IsSubsetOf(elves[1]):
		// 	subsetCount++
		// case elves[1].IsSubsetOf(elves[0]):
		// 	subsetCount++			
		// }

		// Part 2 solution

		// Count range overlaps.
		switch {
		case elves[0].Overlaps(elves[1]):
			subsetCount++
		case elves[1].Overlaps(elves[0]):
			subsetCount++			
		}

	}

	if err = scanner.Err(); err != nil {
        log.Fatal(err)
    }

	// Return subset count.
	return subsetCount
}

// Types.

type pair struct {
	from, to int
}

// Challenge-specific functions.

// Part 1
// Check if current pair subset of other pair.
func (p *pair) IsSubsetOf(other *pair) bool {
	return other.from <= p.from && p.to <= other.to
}

// Part 2
// Check if endpoint of either range falls within other range.
func (p *pair) Overlaps(other *pair) bool {
	switch {
	case other.from <= p.from && p.to <= other.to:
		return true
	case other.from <= p.from && p.from <= other.to:
		return true
	case p.from <= other.from && other.from <= p.to:
		return true
	default:
		return false
	}
}

// Split section range and convert into integer.
// Create and return pair struct from integer duo.
func getPair(s string) *pair {
	var tmp []string
	tmp = strings.Split(s, "-")
	return &pair{
		from: stringToInt(tmp[0]),
		to:   stringToInt(tmp[1]),
	}
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
