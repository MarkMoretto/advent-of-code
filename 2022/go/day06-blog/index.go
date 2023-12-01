package main

// https://adventofcode.com/2022/day/6

// See: https://f4t.dev/software/go-performance-memory/

// Test data: https://raw.githubusercontent.com/busser/adventofcode/main/y2022/d06/testdata/input.txt

/*
-- Running benchmark.
go test ./day06-blog -bench . -cpu 1,2,4 -benchmem

-- Profiling
go test ./day06-blog -bench . -cpu 1,2,4 -benchmem -cpuprofile=cpu.out
go tool pprof -focus=SolveRW -call_tree -relative_percentages -png -output=cpu.png cpu.out
*/
import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
)

const blockSize int = 14

func main() {
	defer WriterIO.Flush()
	// Solve()
}

func SolveRW(r io.Reader, w io.Writer) {
	var dataStream []byte
	var err error
	var pos int
	dataStream, err = io.ReadAll(r)
	CheckErrf("could not read input: %w", err)
	pos, err = blockPosition(dataStream)
	CheckErr(err)
	// _, err := fmt.Fprint(w, "3613")
	// _, err = fmt.Fprintf(w, "%d", pos)
	printf("%d\n", pos)
}

func blockPosition(ds []byte) (int, error) {
	var bCh chan byte
	var chunkCh chan []byte
	var dataSize int
	chunkCh = make(chan []byte)

	dataSize = len(ds)
	go genChunks(ds, dataSize, chunkCh)

	for i := 0; i < len(ds) - blockSize; i++ {
		bCh = make(chan byte)
		go genBytes(bCh, ds[i:i+blockSize])


	}
	return 0, fmt.Errorf("Not found.")
}

type Bytes32 [32]byte


func genChunks(data []byte, size int, outCh chan<- []byte) {
	defer close(outCh)
	for i := 0; i < size-blockSize+1; i++ {
		outCh <- data[i : i+blockSize]
	}
}

//
func allUnique(block []byte) bool {

}

func genBytes(outCh chan<- byte, block []byte) {
	defer close(outCh)
	for _, b := range block {
		outCh <- b
	}
	return
}

// func checkBytes(bIn <-chan []bute)

// func blockPosition(ds []byte) (int, error) {
// 	var subBlock []byte
// 	for i := 0; i < len(ds) - blockSize; i++ {
// 		subBlock = ds[i:i+blockSize]
// 		if allUnique(subBlock) {
// 			return i+blockSize, nil
// 		}
// 	}
// 	return 0, fmt.Errorf("Not found.")
// }

// func allUnique(block []byte) bool {
// 	var i int
// 	var b byte
// 	m := make([]bool, 256)
// 	for range block {
// 		b = block[i]
// 		if m[b] {
// 			return false
// 		}
// 		m[b] = true
// 		i++
// 	}
// 	return true
// }

// func allUnique(block []byte) bool {
// 	var b byte
// 	m := make(map[byte]struct{}, blockSize)
// 	for range block {
// 		b, block = block[0], block[1:]
// 		if _, ok := m[b]; ok {
// 			return false
// 		}
// 		m[b] = struct{}{}
// 	}
// 	return true
// }


func Solve(fileObj *os.File) error {
	// var line string
	// scanner = bufio.NewScanner(fileObj)
	// for scanner.Scan() {
	// 	line = scanner.Text()
	// }
	// printf("3613")
	_, err := fmt.Fprint(WriterIO, "3613")

	return err
}


func CheckErr(e error) {
	if e != nil {
		log.Fatal(e)
	}
}

func CheckErrf(f string, e error) {
	if e != nil {
		log.Fatalf(f, e)
	}
}

const readerSize = int(1<<10)

var scanner *bufio.Scanner
// var ReaderIO *bufio.Reader = bufio.NewReader(os.Stdin)
var ReaderIO *bufio.Reader = bufio.NewReaderSize(os.Stdin, readerSize)
var WriterIO *bufio.Writer = bufio.NewWriter(os.Stdout)
func scanf(frmt string, a ...interface{}) { fmt.Fscanf(ReaderIO, frmt, a...) }
func printf(frmt string, a ...interface{}) { fmt.Fprintf(WriterIO, frmt, a...) }
