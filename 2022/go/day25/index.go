package main

// https://adventofcode.com/2022/day/10

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

	return
}

// Main solver function.
func solve(f *os.File) {
	defer f.Close()
	var (
		line string
		tot int64
	)

	scanner = bufio.NewScanner(f)
	for scanner.Scan() {
		line = scanner.Text()
		tot += snafuToDec[int64](line)
	}
	
	printf("%d\n", tot)
	printf("%s\n", decToSnafu(tot))

}

// Integer type interface for all signed integers.
type Int interface {
	int | int32 | int64
}


const (
	// String (byte slice) for easy indexing when appending to solution.
	availableChars string = `=-012`
)

// Get decimal value for provided byte.
func getValue[N Int](b byte) N {
	switch {
	case b =='-':
		return -1
	case b == '=':
		return -2
	default:
		return N(b - '0')
	}
}

// Convert SNAFU to decimal value.
func snafuToDec[N Int](str string) N {
	var b byte
	var n N
	n = N(len(str))
	if n == 0 {
		return 0
	}
	b = str[n-1]
	return 5 * snafuToDec[N](str[:n-1]) + getValue[N](b)
}

// Convert decimal value to SNAFU.
func decToSnafu[N Int](num N) string {
	if num <= 0 {
		return ""
	}
	q, r := DivMod(num+2, 5)
	return decToSnafu(q) + string(availableChars[r])
}

// divmod() implemented with some light generics.
func DivMod[N Int](base, expon N) (N, N) {
	return base/expon, base%expon
}


// var bbuffr *bytes.Buffer
var scanner *bufio.Scanner
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
