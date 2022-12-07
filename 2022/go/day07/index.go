package main

// https://adventofcode.com/2022/day/7

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

// Max number of lines in data file.
const MaxLines = int(2e4)

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
	var line string
	scanner = bufio.NewScanner(f)
	var currLvl int
	var rootDirectory *Directory
	// var currentDir *Directory

	rootDirectory = newDirectory("/", currLvl)
	rootDirectory.subDirs = make([]*Directory, 0, 100)

	for scanner.Scan() {
		line = scanner.Text()

		switch {
		// change dir
		case line[0:4] == "$ cd":
			switch line[5] {
			// Move up one dir
			case '.':
			// Move to parent dir.
			if currLvl > 0 {
				currLvl--
			}
			case '/':
				// currentDir = rootDirectory
				currLvl = 0
			}

		// List files and subdirectories
		case line[0:4] == "$ ls":

		// Check if directory
		case line[0:5] == "$ dir":
		}

		printf("%s\n", line)
	}
}


type File struct {
	name string
	size int
}


type Directory struct {
	name string
	level int
	subDirs []*Directory
	files []*File
}

func newFile(name string, size int) *File {
	return &File{name, size}
}

func newDirectory(name string, level int) *Directory {
	return &Directory{
		name: name,
		level: level,
	}
}

// BFS
func directoryBfs(rootDir *Directory, name string) *Directory {
	var nextDir *Directory
	q := make([]*Directory, 0, 100)
	q = append(q, rootDir)
	for len(q) > 0 {
		nextDir, q = q[0], q[1:]
		if nextDir.name == name {
			return nextDir
		}
		if len(nextDir.subDirs) > 0 {
			for _, subDir := range nextDir.subDirs {
				q = append(q, subDir)
			}
		}
	}
	return nil
}

// DFS
func directoryDfs(rootDir *Directory, name string) *Directory {
	if rootDir.name == name {
		return rootDir
	}
	if len(rootDir.subDirs) > 0 {
		for _, subDir := range rootDir.subDirs {
			directoryDfs(subDir, name)
		}
	}
	return nil
}



var scanner *bufio.Scanner
var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanws(a ...interface{}) { fmt.Fscan(reader, a...) }
