package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

const (
	DataFilePath = "./data.in"
)

func main() {
	defer writer.Flush()
	var (
		f   *os.File
		err error
		txt string

		a []string
		// rpl *strings.Replacer
		tot               int
		newNum            int
		firstIdx, lastIdx int
		mxSz              int
	)

	a = make([]string, 0, 1e6)

	// File IO
	f, err = os.Open(DataFilePath)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		txt = scanner.Text()
		a = append(a, txt)
		sz := len(txt)
		if sz > mxSz {
			mxSz = sz
		}
	}
	if err := scanner.Err(); err != nil {
		fmt.Println(err)
		return
	}

	// Part 1 -> 54450
	// for _, s := range a {
	//     firstIdx := strings.IndexFunc(s, unicode.IsNumber)
	//     lastIdx := strings.LastIndexFunc(s, unicode.IsNumber)
	//     newNum := stringToInt(string(s[firstIdx]) + string(s[lastIdx]))
	//     tot += newNum
	// }
	// printf("%d\n", tot)

	// Part 2 -> 54265
	// tot = 0
	// nums := make([]int, 0, 1e3+1)
	// rpl = strings.NewReplacer(
	//     "one",   "x1y",
	//     "two",   "x2y",
	//     "three", "x3y",
	//     "four",  "x4y",
	//     "five",  "x5y",
	//     "six",   "x6y",
	//     "seven", "x7y",
	//     "eight", "x8y",
	//     "nine",  "x9y",
	// )
	m := map[string]string{
		"one":   "o1e",
		"two":   "t2o",
		"three": "t3e",
		"four":  "f4r",
		"five":  "f5e",
		"six":   "s6x",
		"seven": "s7n",
		"eight": "e8t",
		"nine":  "n9e",
	}

	for _, s := range a {
		for k, v := range m {
			s = strings.ReplaceAll(s, k, v)
		}
		firstIdx = strings.IndexFunc(s, unicode.IsNumber)
		lastIdx = strings.LastIndexFunc(s, unicode.IsNumber)
		newNum = stringToInt(string(s[firstIdx]) + string(s[lastIdx]))
		tot += newNum
		// printf("%*s %*s  (%2d, %2d) -> %2d | %d\n", mxSz, s, 12, ss, firstIdx, lastIdx, newNum, tot)
	}
	printf("%d\n", tot)
}

func stringToInt(s string) int {
	var out int
	b := []byte(s)
	for _, el := range b {
		out = out*10 + int(el-'0')
	}
	return out
}

const DefaultReaderSize int = 1e2 + 1

var (
	reader *bufio.Reader = bufio.NewReaderSize(os.Stdin, DefaultReaderSize)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	// scnr *bufio.Scanner = bufio.NewScanner(os.Stdin)
)

func printf(f string, a ...interface{}) {
	fmt.Fprintf(writer, f, a...)
}
func scanws(a ...interface{}) {
	fmt.Fscan(reader, a...)
}
