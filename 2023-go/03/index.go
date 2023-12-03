package main

import (
	"bufio"
	"fmt"
	"os"
    _"regexp"
	_"strings"
    _"unicode"
)

const (
	// DataFilePath = "./data.in"
    DataFilePath = "./example-data.in"
)



func main() {
	defer writer.Flush()
	var (
		f   *os.File
		err error
		txt string
		strs []string
	)

	strs = make([]string, 0, 1e6)

	// ff := func(c rune) bool {
	// 	return !unicode.IsLetter(c) && !unicode.IsNumber(c)
	// }

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

    // us-express-app-2023.morbin-123@spamgourmet.com

    // Dimensions
    // l, w := len(strs), len(strs[0])

	// // Part 1
    // var maxTally *CubeTally
    // var gameNo int
    // var tot int
    // var okRonud bool
    // mct := MaxCubeTally()
    // gameNo = 1
	// for _, s := range strs {
    //     arr1 := strings.Split(s, ":")
    //     okRonud = true
    //     for _, reveal := range strings.Split(strings.TrimSpace(arr1[1]), ";") {
    //         rgbArr := strings.FieldsFunc(reveal, ff)
    //         for i := 0; i < len(rgbArr)-1; i++ {
    //             v := stringToInt(rgbArr[i])
    //             switch rgbArr[i+1] {
    //             case "red":
    //                 if v > mct.r {
    //                     okRonud = false
    //                     break
    //                 }
    //             case "blue":
    //                 if v > mct.b {
    //                     okRonud = false
    //                     break
    //                 }
    //             case "green":
    //                 if v > mct.g {
    //                     okRonud = false
    //                     break
    //                 }
    //             default:
    //                 if !okRonud{
    //                     break
    //                 }
    //                 // continue
    //             }
    //         }}

    //     if okRonud {
    //         tot += gameNo
    //     }
    //     gameNo++
	// }
	// printf("%d\n", tot)



}


func allDirections() [][2]int {
    return [][2]int{
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1},
        {-1, -1},
        {-1, 1},
        {1, -1},
        {1, 1},
    }
}

func isDigit[RB rune | byte](r RB) bool {
    return r >='0' && r <= '9'
}
func isNum(s string) bool {
    for _, el := range s {
        if el <'0' || el > '9' {
            return false
        }
    }
    return true
}

func Part1(a []string, h, w int) {
    var i, j int
    okNums := make([]int, 0, 1e6)
    var isOk bool
    for _, line := range a {
        isOk = false
        i = 0
        for i < h-1 {
            j = i + 1
            for j < w && isDigit(line[j]) {
                if isOk {
                    continue
                }
                for _, d := range allDirections() {
                    dh, dw := i+d[0], j+d[1]
                    if dh >= h || dh < 0 || dw >= w || dw < 0 {
                        continue
                    }
                    stmp := a[dh]
                    if !isDigit(stmp[dw]) && stmp[dw] != '.' {
                        isOk = true
                        break
                    }
                }
                j++
            }
            if isOk {
                okNums = append(okNums, stringToInt[int](line[i:j]))
            }
        }
    }
    printf("%v\n", okNums)
}


type MostIntegers interface {
    ~int | ~int32 | ~int64 | ~uint | ~uint32 | ~uint64
}

func stringToInt[N MostIntegers](s string) N {
	var out N
	b := []byte(s)
	for _, el := range b {
		out = out*10 + N(el-'0')
	}
	return out
}

func maxInt[N MostIntegers](x, y N) N {
    if x > y { return x }
    return y
}


// const DefaultReaderSize int = 3e2 + 1
var (
	// reader *bufio.Reader = bufio.NewReaderSize(os.Stdin, DefaultReaderSize)
    reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	// scnr *bufio.Scanner = bufio.NewScanner(os.Stdin)
)

func printf(f string, a ...interface{}) {
	fmt.Fprintf(writer, f, a...)
}
func scanws(a ...interface{}) {
	fmt.Fscan(reader, a...)
}
