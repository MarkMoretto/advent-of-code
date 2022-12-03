package main

// https://adventofcode.com/2022/day/3

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
	
	// part 1
	// res = part1(f)
	// printf("%d\n", res)

	// part 2
	res = part2(f)
	printf("%d\n", res)
}

// Part 1 solution

func part1(f *os.File) int {
	defer f.Close()
	var tot int
	var err error
	
	// Scan lines in file.
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		txt := scanner.Text()
		slen := len(txt)

		// Split text in half
		h1, h2 := txt[:slen/2], txt[slen/2:]

		// Find common characters between halves.
		rz := commonChars(h1, h2)

		// For each common character, increment total
		// by specified amount.
		for _, el := range rz {
			tot += priorityValue(el)
		}
	}

	if err = scanner.Err(); err != nil {
        log.Fatal(err)
    }
	
	return tot
}

// Part 2 solution

const ElvesPerGroup = 3

func part2(f *os.File) int {
	defer f.Close()
	var (
		rFreq map[rune]int
		sacks []string
		matches, uniq []rune
		txt string
		err error
		lineCt, tot int
	)

	sacks = make([]string, 0, ElvesPerGroup)

	scanner = bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	lineCt = 1
	for scanner.Scan() {
		txt = scanner.Text()
		sacks = append(sacks, txt)

		// If line count divisible by group count, process data.
		if lineCt % ElvesPerGroup == 0 {

			// Create slice and map for new matches and counts.
			matches = make([]rune, 0, ElvesPerGroup)
			rFreq = make(map[rune]int, ElvesPerGroup)

			for _, sack := range sacks {

				// Get unique characters for string.
				uniq = uniqueChars(sack)

				// Iterate over unique characters.
				for _, r := range uniq {
					// Increment map value by one.
					rFreq[r]++

					// If count of character equals number of elves in group,
					// add character to slice.
					if rFreq[r] == ElvesPerGroup {
						matches = append(matches, r)
					}					
				}
			}

			// Add value of any characters to total amount.
			for _, el := range matches {
				tot += priorityValue(el)
			}

			// Create new sacks slice and proceed to next series of iterations.
			sacks = make([]string, 0, ElvesPerGroup)
		}

		lineCt++
	}

	if err = scanner.Err(); err != nil {
        log.Fatal(err)
    }
		
	return tot
}

// Functions.

// Return priority value for provided character.
func priorityValue(r rune) int {
	switch {
	case 'a' <= r && r <= 'z':
		return int(r - 'a') + 1
	default:
		return int(r - 'A') + 27
	}
}

// Return map collection with count of each character in string.
func getFreqMap(s string) map[rune]int {
	n := len(s)
	fMap := make(map[rune]int, n)
	for _, ch := range s {
		fMap[ch]++
	}
	return fMap
}

// Find unique common characters between two strings.
func commonChars(s1, s2 string) []rune {
	out := make([]rune, 0, 1e5)
	fMap1, fMap2 := getFreqMap(s1), getFreqMap(s2)
	for k := range fMap1 {
		if _, ok := fMap2[k]; ok {
			out = append(out, k)
		}
	}
	return out
}

// Return unique characters from string.
func uniqueChars(s string) []rune {
	n := len(s)
	outMap := make(map[rune]bool, n)
	outSlice := make([]rune, 0, n+1)
	rz := []rune(s)
	for _, el := range rz {
		if _, ok := outMap[el]; !ok {
			outMap[el] = true
			outSlice = append(outSlice, el)
		}
	}
	return outSlice
}

// func allUniqueChars(strs ...string) []rune {
// 	var outs []rune
// 	var m map[rune]bool
// 	m = map[rune]bool{}
// 	for _, str := range strs {
// 		for _, r := range str {
// 			if _, ok := m[r]; !ok {
// 				m[r] = true
// 				outs = append(outs, r)
// 			}
// 		}
// 	}
// 	return outs
// }

// Handle multiple strings as parameter.
// func manyCmmonChars(strs ...string) []rune {
// 	out := make([]rune, 0, 1e5)
// 	nStrs := len(strs)
// 	if nStrs <= 0 {
// 		return nil
// 	}

// 	fMap := make(map[rune]int, nStrs)
// 	for _, str := range strs {
// 		for _, el := range str {
// 			if _, ok := fMap[el]; ok {
// 				out = append(out, el)
// 			}
// 		}
// 	}

// 	return out
// }

// Count lines in file.
// func lineCounter(f *os.File) (int, error) {
// 	var buffr, lineSep []byte
// 	var cnt int
// 	const KB int = int(1<<10)

// 	lineSep = []byte("\n") // []byte{'\n'}
// 	buffr = make([]byte, 32*KB)

// 	for {
// 		idx, err := f.Read(buffr)
// 		switch {
// 		case err == io.EOF:
// 			return cnt, nil
// 		case err != nil:
// 			return cnt, err
// 		}
// 		cnt = cnt + bytes.Count(buffr[:idx], lineSep)
// 	}
// }

// View map object.
func viewMap(m map[rune]int) {
	for k, v := range m {
		printf("%s: %d\n", string(k), v)
	}	
}

var scanner *bufio.Scanner
var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanws(a ...interface{}) { fmt.Fscan(reader, a...) }
