package main

// https://adventofcode.com/2023/day/3

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
	_ "strings"
	_ "unicode"
)

const (
	DataFilePath = "./data.in"
	// DataFilePath    = "./example-data.in"
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

// Solution dispatch
type SolutionFn func([]string)

func SolutionRunner(sarr []string, f SolutionFn) {
	f(sarr)
}

// Solutions

func Part1(lines []string) {
	var neighbors, symbEdges []*Edge
	var edgeMap map[*Edge][]int
	var start, stop, tot, num int
	edgeMap = make(map[*Edge][]int, DefaultSliceCap)
	symbEdges = getEdgesOnlySymbols(lines)
	hasEdge := containsEdge(symbEdges)
	p := regexp.MustCompile(`\d+`)
	for r, line := range lines {
		for _, res := range p.FindAllStringIndex(line, -1) {
			if len(res) == 0 {
				continue
			}
			// Create neighbors
			start, stop = res[0], res[1]
			num = stringToInt(line[start:stop])
			neighbors = make([]*Edge, 0, DefaultSliceCap)
			for _, i := range []int{r - 1, r, r + 1} {
				for j := start - 1; j <= stop; j++ {
					neighbors = append(neighbors, &Edge{i, j})
				}
			}
			for _, neigh := range neighbors {
				if hasEdge(neigh) {
					if _, ok := edgeMap[neigh]; !ok {
						edgeMap[neigh] = make([]int, 0, DefaultSliceCap)
					}
					edgeMap[neigh] = append(edgeMap[neigh], num)
				}
			}
		}
	}
	for _, n := range edgeMap {
		tot += sumInts(n)
	}
	printf("%d\n", tot)
}

// print(sum(map(prod, filter(lambda q: len(q) == 2, char_edges.values()))))
func Part2(lines []string) {
	var neighbors, symbEdges []*Edge
	var edgeMap map[Edge][]int
	var start, stop, tot, num int
	edgeMap = make(map[Edge][]int, DefaultSliceCap)
	symbEdges = getEdgesOnlySymbols(lines)
	hasEdge := containsEdge(symbEdges)
	p := regexp.MustCompile(`\d+`)
	for r, line := range lines {
		for _, res := range p.FindAllStringIndex(line, -1) {
			if len(res) == 0 {
				continue
			}
			// Create neighbors
			start, stop = res[0], res[1]
			num = stringToInt(line[start:stop])
			neighbors = make([]*Edge, 0, DefaultSliceCap)
			for _, i := range []int{r - 1, r, r + 1} {
				for j := start - 1; j <= stop; j++ {
					neighbors = append(neighbors, &Edge{i, j})
				}
			}
			for _, neigh := range neighbors {
				if hasEdge(neigh) {
					if _, ok := edgeMap[*neigh]; !ok {
						edgeMap[*neigh] = make([]int, 0, DefaultSliceCap)
					}
					edgeMap[*neigh] = append(edgeMap[*neigh], num)
				}
			}
		}
	}

	for _, n := range edgeMap {
        // printf("%v  %v\n", k, n)
        if len(n) == 2 {
            tot += multInts(n)
        }

	}
	printf("%d\n", tot)
}

// Edge and related.
type Edge struct {
	r, c int
}

// Compare edges.
func (q *Edge) isEqualTo(other *Edge) bool {
	return q.r == other.r && q.c == other.c
}

// Check slice of edges for existing edge.
func containsEdge(edges []*Edge) func(*Edge) bool {
	return func(edge *Edge) bool {
		for _, e := range edges {
			if edge.isEqualTo(e) {
				return true
			}
		}
		return false
	}
}

// Return list of edges that are not numeric or a period character.
func getEdgesOnlySymbols(sarr []string) []*Edge {
	var Ignore = `0123456789.`
	o := make([]*Edge, 0, 1e6)
	for i := range sarr {
		for j, el := range sarr[i] {
			if !hasChar(Ignore, el) {
				o = append(o, &Edge{i, j})
			}
		}
	}
	return o
}

func hasChar[RB rune | byte](str string, rb RB) bool {
	return strings.ContainsRune(str, rune(rb))
}

func stringToInt(s string) int {
	var out int
	b := []byte(s)
	for _, el := range b {
		out = out*10 + int(el-'0')
	}
	return out
}

func maxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func sumInts(nums []int) int {
    o := nums[0]
	for _, n := range nums[1:] {
		o += n
	}
	return o
}

func multInts(nums []int) int {
    o := 1
    for _, num := range nums {
        o *= num
    }
    return o
}

// IO
const (
	DefaultReaderSize int = 2e2
)

var (
	reader *bufio.Reader = bufio.NewReaderSize(os.Stdin, DefaultReaderSize)
	// reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	// scnr *bufio.Scanner = bufio.NewScanner(os.Stdin)
)

func printf(f string, a ...interface{}) {
	fmt.Fprintf(writer, f, a...)
}
func scanws(a ...interface{}) {
	fmt.Fscan(reader, a...)
}
