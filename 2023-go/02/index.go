package main

import (
	"bufio"
	"fmt"
	"os"
    _ "regexp"
	"strings"
    "unicode"
)

const (
	DataFilePath = "./data.in"
    // DataFilePath = "./example-data.in"
)

type CubeTally struct {
    r, g, b int
}

func MaxCubeTally() *CubeTally {
    return &CubeTally{12, 13, 14}
}

func (m *CubeTally) hasOkTally() bool {
    mct := MaxCubeTally()
    return m.r <= mct.r && m.g <= mct.g && m.b <= mct.b
}

func main() {
	defer writer.Flush()
	var (
		f   *os.File
		err error
		txt string
		strs []string
        gameNo int
	)

	strs = make([]string, 0, 1e6)

	ff := func(c rune) bool {
		return !unicode.IsLetter(c) && !unicode.IsNumber(c)
	}

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


	// Part 2
    var tot uint32
    gameNo = 1
	for _, s := range strs {
        arr1 := strings.Split(s, ":")
        maxTally := [3]uint32{}
        // Iterate over each cube Reveal and evaluate max value for each color.
        for _, reveal := range strings.Split(strings.TrimSpace(arr1[1]), ";") {
            rgbArr := strings.FieldsFunc(reveal, ff)
            for i := 0; i < len(rgbArr)-1; i += 2 {
                v := stringToInt[uint32](rgbArr[i])
                color := rgbArr[i+1]
                // Get first char from string.
                switch color[0] {
                case 'r':
                    maxTally[0] = maxInt(maxTally[0], v)
                case 'b':
                    maxTally[1] = maxInt(maxTally[1], v)
                case 'g':
                    maxTally[2] = maxInt(maxTally[2], v)
                default:
                    continue
                }
            }
        }
        // Add product to total
        tot += rgbProduct(maxTally)
        gameNo++
	}
	printf("%d\n", tot)
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
    if x > y { return x }
    return y
}

func rgbProduct[N ~uint | ~uint32 | ~uint64](rgb [3]N) N {
    var t N
    t = 1
    for _, el := range rgb {
        t *= el
    }
    return t
}

const DefaultReaderSize int = 3e2 + 1
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
