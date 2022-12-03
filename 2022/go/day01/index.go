package main

// https://adventofcode.com/2022/day/1

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
)

func main() {
	defer writer.Flush()
	var txt string
	var subSum, tot int
	var calories []int

	f, err := os.Open("day01/data.in")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	
	// part 1
	// var mx int
	// mx = -1
	// scanner := bufio.NewScanner(f)
	// for scanner.Scan() {
	// 	txt = scanner.Text()
	// 	if len(txt) == 0 {
	// 		mx = MaxInt(mx, subSum)
	// 		subSum = 0
	// 		continue
	// 	}
	// 	subSum = subSum + stringToInt(txt)
	// }

	// Part 2
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		txt = scanner.Text()
		if len(txt) == 0 {
			calories = append(calories, subSum)
			subSum = 0
			continue
		}
		subSum = subSum + stringToInt(txt)
	}	

	if err := scanner.Err(); err != nil {
        fmt.Println(err)
    }

	sort.Sort(sort.Reverse(sort.IntSlice(calories)))

	for _, el := range calories[:3] {
		tot += el
	}
	printf("%d\n", tot)
}


func stringToInt(s string) int {
	var out int
	b := []byte(s)
	for _, el := range b {
		out = out * 10 + int(el - '0')
	}
	return out
}

func MinInt(x, y int) int {
	if y > x {
		return x
	}
	return y
}

func MaxInt(x, y int) int {
	if y > x {
		return y
	}
	return x
}


var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanws(a ...interface{}) { fmt.Fscan(reader, a...) }
