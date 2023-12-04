package main

// https://adventofcode.com/2023/day/4

import (
	"bufio"
	"fmt"
	"os"
	_ "regexp"
	"strings"
    _"sort"
	_ "unicode"
)

const (
	DataFilePath = "./data.in"
	// DataFilePath = "./example-data.in"
	DefaultSliceCap = 1e6
)

func main() {
	defer writer.Flush()
	var (
		f    *os.File
		err  error
		txt  string
		strs []string
	)

	strs = make([]string, 0, DefaultSliceCap)

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
		strs = append(strs, txt)
	}
	if err := scanner.Err(); err != nil {
		fmt.Println(err)
		return
	}

	// Solutions

    // SolutionRunner(strs, Part1)

    SolutionRunner(strs, Part2)

}

type SolutionFn func([]string)

func SolutionRunner(sarr []string, f SolutionFn) {
    f(sarr)
}


func Part1(lines []string) {
	var totPts int
    var nCorrect int
	for _, line := range lines {
        nCorrect = 0
		items := strings.Split(line, ":")
		numbers := strings.Split(items[1], "|")
		winstr, havestr := trimSpace(numbers[0]), trimSpace(numbers[1])
		wins, haves := strings.Fields(winstr), strings.Fields(havestr)
		for _, num := range haves {
			if Some(wins, func(x string) bool { return x == num }) {
                nCorrect++
			}
		}
        if nCorrect > 0 {
            totPts += (1 * 1<<(nCorrect-1))
        }
	}
	printf("%d\n", totPts)
}

func Part2(lines []string) {
	var totPts int
    var nCorrect int
    nCards := len(lines)
    rewards := make([]int, nCards)
    for j := range rewards {
        rewards[j] = 1
    }
	for cardNo, line := range lines {
        nCorrect = 0
		items := strings.Split(line, ":")
		numbers := strings.Split(items[1], "|")
		winstr, havestr := trimSpace(numbers[0]), trimSpace(numbers[1])
		wins, haves := strings.Fields(winstr), strings.Fields(havestr)
		for _, num := range haves {
			if Some(wins, func(x string) bool { return x == num }) {
                nCorrect++
			}
		}
        if nCorrect > 0 {
            // totPts += (1 * 1<<(nCorrect-1))
            for i := cardNo; i < cardNo+nCorrect; i++ {
                if i+1 < nCards {
                    rewards[i+1] += rewards[cardNo]
                }
            }
        }
	}
    for _, c := range rewards {
        totPts += c
    }
	printf("%d\n", totPts)
}


func stringToIntSlice(s string) []int {
	o := make([]int, 0, len(s))
	for _, el := range strings.Split(trimSpace(s), " ") {
		o = append(o, stringToInt[int](el))
	}
	return o
}

func stringToInt[N ~int | ~int32 | ~int64 | ~uint | ~uint32 | ~uint64](s string) N {
	var out N
	b := []byte(s)
	for _, el := range b {
		out = out*10 + N(el-'0')
	}
	return out
}

func maxInt[N ~int | ~int32 | ~int64 | ~uint | ~uint32 | ~uint64](x, y N) N {
	if x > y {
		return x
	}
	return y
}

func Some(items []string, f func(string) bool) bool {
	for _, item := range items {
		if f(item) {
			return true
		}
	}
	return false
}

func trimSpace(s string) string {
    return strings.TrimSpace(s)
}

func splitOnSpace(s string) []string {
    return strings.Split(s, " ")
}

const (
    DefaultReaderSize int = 3e2 + 1
)

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
