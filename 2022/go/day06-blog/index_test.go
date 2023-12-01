package main

// https://www.golinuxcloud.com/golang-benchmark/

import (
	"bytes"
	"io"
	_ "log"
	"os"
	"testing"
)

const filePathData = `./data.in`

func DemoDay06() {
	f, err := os.Open(filePathData)
	CheckErr(err)
	defer f.Close()

	SolveRW(f, os.Stdout)

	// if err := SolveRW(f, os.Stdout); err != nil {
	// 	log.Fatalf("Count not solve: %v\n", err)
	// }
}

func Benchmark(b *testing.B) {
	i, e := os.ReadFile(filePathData)
	CheckErrf("Could not read data file: %v\n", e)
	rdr := bytes.NewReader(i)
	wrt := io.Discard
	for n := 0; n < b.N; n++ {
		rdr.Reset(i)
		SolveRW(rdr, wrt)
	}
}
