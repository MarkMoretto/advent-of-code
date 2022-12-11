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

	return
}

const (
	MaxCapacity = 1e3
	Width = 40
	Height = 6
)

type Register int
type Registers []Register

func (r Register) ToInt() int { return int(r) }
func (r Registers) Len() int { return len(r) }


// Main solver function.
func solve(f *os.File) {
	defer f.Close()

	var (
		parts []string
		registers Registers
		line string
		cmd string
		amt Register
		x Register
	)

	registers = make(Registers, 0, MaxCapacity)
	registers = append(registers, 0)
	registers = append(registers, 1)
	x = 1
	scanner = bufio.NewScanner(f)
	for scanner.Scan() {
		line = scanner.Text()
		parts = strings.Fields(line)

		cmd = parts[0]

		if cmd[0] == 'n' {
			registers = append(registers, x)
			continue
		}

		amt = strToRegister(parts[1])
		// printf("amt: %d Reg len: %d\n", amt, registers.Len())
		// printf("amt: %d ", amt)
		x = registers[registers.Len()-1]
		// printf("x1: %d ", x)
		registers = append(registers, x)
		x += amt
		// printf("x2: %d\n", x)
		registers = append(registers, x)
		// printf("x: %d\n", x)
	}

	for ptr := range registers {
		printf("%d %d\n", ptr, registers[ptr])
		// if ptr%20==0 {
		// 	printf("%d\n", registers[ptr])
		// } else {
		// 	printf("%d\n", registers[ptr])
		// }
	}

	// Part 1
	part1(registers)
}

func part1(rz Registers) {
	var p Register
	var totSignalStrength Register
	for p = 0; p.ToInt() < rz.Len(); p++ {
		if p >= 20 && (p-20)%40==0 {
			totSignalStrength += (p*rz[p])
		}
	}
	printf("%d\n", totSignalStrength)
}

func strToRegister(s string) Register {
	var isNeg bool
	if s[0] == '-' {
		isNeg = true
	}
	s = s[1:]
	n := strToInt(s)
	if isNeg {
		n = -n
	}
	return Register(n)
}

func strToInt(s string) int {
	var out int
	for _, el := range s {
		out = out * 10 + int(el - '0')
	}
	return out
}

var scanner *bufio.Scanner
var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanws(a ...interface{}) { fmt.Fscan(reader, a...) }
