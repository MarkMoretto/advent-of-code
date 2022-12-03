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
		txt string
		err error
		slen int		
	)

	// Get data path.
	if len(os.Args) > 1 {
		dataPath = os.Args[1]
	}

	f, err = os.Open(dataPath)
	if err != nil {
		log.Fatal(err)
	}
	// defer f.Close()
	
	// part 1
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		txt = scanner.Text()
		slen = len(txt)
		h1, h2 := txt[:slen/2], txt[slen/2:]
		// printf("%s  %s\n", h1, h2)
		printf("%v\n", commonChars(h1, h2))
	}


	if err = scanner.Err(); err != nil {
        log.Fatal(err)
    }

	if err = f.Close(); err != nil {
		log.Fatal(err)
	}
}

func getFreqMap(s string) map[rune]int {
	n := len(s)
	fMap := make(map[rune]int, n)
	for _, ch := range s {
		fMap[ch]++
	}
	return fMap
}

func commonChars(s1, s2 string) []rune {
	out := make([]rune, 0, 1_000)
	fMap1, fMap2 := getFreqMap(s1), getFreqMap(s2)
	for k := range fMap1 {
		if _, ok := fMap2[k]; ok {
			out = append(out, k)
		}
	}
	return out
}


var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanws(a ...interface{}) { fmt.Fscan(reader, a...) }
