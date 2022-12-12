package main

// https://adventofcode.com/2022/day/10

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
		f        *os.File
		dataPath string
		err      error
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

const (
	MaxAnimals   = 10
	MatchPattern = `\d+`
	Part1Rounds = 20
	Part2Rounds = 10_000
)


// Main solver function.
func solve(f *os.File) {
	defer f.Close()

	var (
		monkies   []*Monkey
		monk      *Monkey
		allInspections []int
		line      string
		nRounds   int
		worryItem int
		modDivisor int
		isPart1 bool
	)

	monkies = make([]*Monkey, 0, MaxAnimals)
	allInspections = make([]int, 0, MaxAnimals)

	scanner = bufio.NewScanner(f)
	for scanner.Scan() {

		line = scanner.Text()

		switch {
		case len(strings.TrimSpace(line)) == 0:
			monkies = append(monkies, monk)
		case strings.Contains(line, "Monkey"):
			monk = newMonkey()
		default:
			updateMonkey(line, monk)
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}

	monkies = append(monkies, monk)

	isPart1 = false

	// LCM
	modDivisor = 1
	for _, m := range monkies {
		// lcmDivisor = LCM(lcmDivisor, m.testDiv)
		modDivisor *= m.testDiv
		// printf("%d %d\n", modDivisor, m.testDiv)
	}



	for nRounds < Part2Rounds {
		for i := range monkies {
			cm := monkies[i]
			for cm.hasItems() {
				worryItem, cm.items = cm.items[0], cm.items[1:]
				worryLvl := cm.inspection(worryItem) % modDivisor
				cm.nInspections++

				if isPart1 {
					worryLvl = postInspection(worryLvl)
				}

				if worryLvl%cm.testDiv == 0 {
					monkies[cm.tossTrue].items = append(monkies[cm.tossTrue].items, worryLvl)
				} else {
					monkies[cm.tossFalse].items = append(monkies[cm.tossFalse].items, worryLvl)
				}

			}
		}
		nRounds++
	}

	for _, m := range monkies {
		allInspections = append(allInspections, m.nInspections)
	}

	// Sort and print product of top two results.
	HeapSort(allInspections, HeapifyDesc[int])
	printf("%d\n", allInspections[0] * allInspections[1])

}


// Function type signature.
type FnInspection func(int) int


// Main monkey struct.
type Monkey struct {
	items        []int
	inspection   FnInspection
	testDiv      int
	tossTrue     int
	tossFalse    int
	nInspections int
}

// Moneky stringer format.
var fstring string = `items: %v
test: %d
true: %d
false: %d
insp. ct: %d
`

// Stringer method.
func (m *Monkey) String() string {
	return fmt.Sprintf(fstring, m.items, m.testDiv, m.tossTrue, m.tossFalse, m.nInspections)
}

// Create new monkey instance.
func newMonkey() *Monkey {
	return &Monkey{
		items: make([]int, 0, 1e2),
	}
}

//
func postInspection(item int) int {
	return item / 3
}

// Check if items list empty.
func (m *Monkey) hasItems() bool { return len(m.items) > 0 }

// Update current monkey based on string contents.
func updateMonkey(s string, m *Monkey) {
	var parts []string
	var p1, p2 string
	parts = strings.Split(s, ":")
	if len(parts) != 2 {
		return
	}

	p1, p2 = strings.TrimSpace(parts[0]), strings.TrimSpace(parts[1])

	switch {
	case strings.Contains(p1, "Starting items"):
		tmp := splitInts(p2)
		(*m).items = append((*m).items, tmp...)

	case strings.Contains(p1, "Operation"):
		p2 = strings.Replace(p2, "new = old ", "", -1)
		tmp := strings.Split(p2, " ")
		oper, d := string(tmp[0]), string(tmp[1])
		(*m).inspection = setInspection(oper, d)

	case strings.Contains(p1, "Test"):
		p2 = strings.Replace(p2, "divisible by ", "", -1)
		(*m).testDiv = strToInt(strings.TrimSpace(p2))

	case strings.Contains(p1, "If true"):
		p2 = strings.Replace(p2, "throw to monkey ", "", -1)
		(*m).tossTrue = strToInt(strings.TrimSpace(p2))

	case strings.Contains(p1, "If false"):
		p2 = strings.Replace(p2, "throw to monkey ", "", -1)
		(*m).tossFalse = strToInt(strings.TrimSpace(p2))
	}

}

// Split string into integer slice.
func splitInts(intStr string) []int {
	var out []int
	for _, el := range strings.Split(intStr, ",") {
		tmp := strings.TrimSpace(el)
		out = append(out, strToInt(tmp))
	}
	return out
}

// Operator closure.
func setInspection(op, delta string) func(int) int {
	var f func(int, int) int
	switch op {
	case "+":
		f = func(a, b int) int { return a + b }
	case "-":
		f = func(a, b int) int { return a - b }
	case "*":
		f = func(a, b int) int { return a * b }
	case "/":
		f = func(a, b int) int { return a / b }
	}
	return func(old int) int {
		if delta == "old" {
			return f(old, old)
		} else {
			return f(old, strToInt(delta))
		}
	}
}

func strToInt(s string) int {
	var out int
	for _, el := range s {
		out = out*10 + int(el-'0')
	}
	return out
}

// ~~~ Sorting method ~~~

// Integer number generic.
type Number interface {
	~int
}

// Heapify type (signature).
type HeapifyMethod[X Number]func([]X, X, X)

func HeapSort[X Number](numSlice []X, fn ...HeapifyMethod[X]) {
	var nElements X
	var heapFunc HeapifyMethod[X]

	switch len(fn) {
	case 1:
		heapFunc = fn[0]
	case 0:
		heapFunc = HeapifyAsc[X]
	default:
		return
	}

	nElements = X(len(numSlice))
	for i := (nElements / 2) - 1; i >= 0; i-- {
		heapFunc(numSlice, nElements, i)
	}
	for j := nElements - 1; j >= 0; j-- {
		numSlice[0], numSlice[j] = numSlice[j], numSlice[0]
		heapFunc(numSlice, j, 0)
	}
}

// Sort ascending.
func HeapifyAsc[X Number](arr []X, n, i X) {
	largest, left, right := i, 2*i+1, 2*i+2

	if left < n && arr[left] > arr[largest] {
		largest = left
	}

	if right < n && arr[right] > arr[largest] {
		largest = right
	}

	if largest != i {
		arr[i], arr[largest] = arr[largest], arr[i]
		HeapifyAsc(arr, n, largest)
	}
}

// Sort descending.
func HeapifyDesc[X Number](a []X, n, i X) {

	smallest, left, right := i, 2*i+1, 2*i+2

	if left < n && a[left] < a[smallest] {
		smallest = left
	}

	if right < n && a[right] < a[smallest] {
		smallest = right
	}

	if smallest != i {
		a[i], a[smallest] = a[smallest], a[i]
		HeapifyDesc(a, n, smallest)
	}
}


var scanner *bufio.Scanner
var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanws(a ...interface{})           { fmt.Fscan(reader, a...) }


// // Merge sort

// // Number constraint (go 1.18+)
// type Number interface {
// 	int | int32 | int64
// }

// // Merge sort function.
// func MergeSort[N Number](numSlice []N) []N {
// 	switch len(numSlice) {
// 	case 0:
// 		return nil
// 	case 1, 2:
// 		return merge(numSlice[:1], numSlice[1:])
// 	default:
// 		lCh, rCh := make(chan []N), make(chan []N)
// 		sz := len(numSlice) / 2
// 		go func() {
// 			lCh <- MergeSort(numSlice[:sz])
// 		}()
// 		go func() {
// 			rCh <- MergeSort(numSlice[sz:])
// 		}()
// 		return merge(<-lCh, <-rCh)
// 	}
// }

// // Merge function
// func merge[N Number](lSlice, rSlice []N) []N {
// 	outs := make([]N, 0, len(lSlice) + len(rSlice))
// 	for len(lSlice) > 0 || len(rSlice) > 0 {
// 		switch {
// 		case len(lSlice) == 0:
// 			outs, rSlice = append(outs, rSlice[0]), rSlice[1:]

// 		case len(rSlice) == 0:
// 			outs, lSlice = append(outs, lSlice[0]), lSlice[1:]

// 		case lSlice[0] <= rSlice[0]:
// 			outs, lSlice = append(outs, lSlice[0]), lSlice[1:]

// 		case lSlice[0] > rSlice[0]:
// 			outs, rSlice = append(outs, rSlice[0]), rSlice[1:]
// 		}
// 	}
// 	return outs
// }


// type BinaryOperation[X Number] func(X, X) X
// func reduce[N Number](accumul N, current N, rest ...interface{}) {
// 	var accumul N
// 	var f BinaryOperation[N]
// 	if len(rest) == 2 {
// 		accumul = rest[0].(N)
// 		f = rest[1].(BinaryOperation[N])
// 	} else {
// 		accumul = rest[0].(N)
// 		f = func(a, b N) N {
// 			return a + b
// 		}
// 	}
// }

// func isBinOp[N Number](obj interface{}) bool {
// 	switch obj.(type) {
// 	case BinaryOperation[N]:
// 		return true
// 	default:
// 		return false
// 	}
// }

// func GCD[N Number](x, y N) N {
// 	if y == 0 {
// 		return x
// 	} else {
// 		return GCD(y, x%y)
// 	}
// }

// func LCM[N Number](x, y N) N {
// 	return x * (y / GCD(x, y))
// }
