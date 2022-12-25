package main

// https://adventofcode.com/2022/day/22

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

}


// Main solver function.
func solve(f *os.File) {
	defer f.Close()

	var (
		cmds []*Command
		line string
		cmdStr string
		boardMap []string
		width, height int
	)

	width = -1
	boardMap = make([]string, 0, 1e3)
	cmds = make([]*Command, 0, 1e6)

	scanner = bufio.NewScanner(f)

	for scanner.Scan() {
		line = scanner.Text()
		height++
		switch {
		case strings.ContainsAny(line, ".#"):
			boardMap = append(boardMap, line)
			if len(line) > width {
				width = len(line)
			}
		case strings.ContainsAny(line, "1234567890LRUD"):
			cmdStr = line
		default:
			continue
		}
	}
	// For command line and blank line
	height -= 2
	printf("W: %d  H: %d\n", width, height)

	// for i, row := range boardMap {
	// 	printf("%d: (%d) => %s\n", i, len(row), row)
	// }

	getCommands(cmdStr, &cmds)
	for _, c := range cmds {
		printf("Amt: %d, Dir: %s\n", c.amount, string(c.direction))
	}
}

type heading struct {
	movement byte
	value int	
}
type Headings map[byte]*heading

func getHeadings() Headings {
	return Headings{
		'R': &heading{'>', 0},
		'D': &heading{'v', 1},
		'L': &heading{'<', 2},
		'U': &heading{'^', 3},
	}
}

func headingDirection(dir byte) byte {
	return getHeadings()[dir].movement
}

func headingValue(dir byte) int {
	return getHeadings()[dir].value
}

type Command struct {
	direction byte
	amount int
}

func getCommands(str string, outc *[]*Command) {
	var tmp []byte
	var chr byte
	var c *Command

	for range str {
		chr, str = str[0], str[1:]
		if isChar(chr) {
			c = &Command{}
			c.direction = chr
			if len(tmp) > 0 {
				c.amount = bytesToInt(tmp)
				(*outc) = append((*outc), c)
				tmp = make([]byte, 0, 10)
			}
		} else {
			tmp = append(tmp, chr)
		}
	}
}

func isChar(r byte) bool {
	return 'A' <= r && r <= 'Z'
}


func calcFinalPassword(r, c, h int) int {
	return 1_000*r + 4*c + h
}

// Conversion
type Int interface {
	~int
}

func strToInt[S string, I Int](s S) I {
	var out I
	for _, el := range s {
		out = out * 10 + I(el - '0')
	}
	return out
}

func bytesToInt(x []byte) int {
	var out int
	for _, b := range x {
		out = out * 10 + int(b - '0')
	}
	return out
}



var scanner *bufio.Scanner
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
