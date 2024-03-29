package main

// https://adventofcode.com/2022/day/9

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

const MaxCumulFileSize = 100_000

// Main solver function.
func solve(f *os.File) {
	defer f.Close()

	var (
		rootDir *Directory
		currentDir *Directory
		currFile *fileObj
		cmds []string
		line string
		currLvl int
		// totDirSize int
	)

	rootDir = newDirectory("/", currLvl)
	currLvl = 0

	scanner = bufio.NewScanner(f)

	for scanner.Scan() {
		line = scanner.Text()

		// Split the line by unicode white space
		cmds = strings.Fields(line)
		// printf("%v\n", cmds)

		switch {
		// change dir
		case cmds[1] == "cd":
			switch cmds[2] {
			// Move up one dir
			case "..":
				// Move to parent dir.
				// if currLvl > 0 {
				// 	currLvl--
				// } else {
				// 	currLvl = 0
				// }

				// Get parent.
				currentDir = rootDir.getParentOf(currentDir)
				currLvl = currentDir.level

			case "/":
				currentDir = rootDir
			
			// cd into specified directory.
			default:
				// currentDir = directoryDfs(currentDir, cmds[2])
				currentDir = directoryBfs(rootDir, cmds[2])
				// currLvl++
				// printf("%s\n", currentDir.name)
			}

		// List files and subdirectories
		case cmds[1] == "ls":
			continue

		// Check if line is directory entry
		case cmds[0] == "dir":
			currLvl++
			tmpDir := newDirectory(cmds[1], currLvl)
			tmpDir.parent = currentDir
			// currentDir.subDirs = append(currentDir.subDirs, tmpDir)
			currentDir.AddSubDir(tmpDir)

		// It is a file with the format: "size filename"
		default:
			fileSize := strToInt(cmds[0])
			// totDirSize += fileSize
			currFile = newFile(cmds[1], fileSize)
			currentDir.files = append(currentDir.files, currFile)
			currentDir.totFileSize += fileSize
		}

		// printf("%s\n", line)
		// printf("%s\n",currentDir)
		// viewTree(rootDir)
	}
	
	// View tree.
	// viewTree(rootDir)

	// Result for part 1
	// printf("%d\n", totDirSize)
	walkDirsAndSumTotal(rootDir, MaxCumulFileSize, 0)
}

func strToInt(s string) int {
	var out int
	for _, el := range s {
		out = out * 10 + int(el - '0')
	}
	return out
}

type fileObj struct {
	name string
	size int
}

func (f *fileObj) String() string {
	return fmt.Sprintf("%s (file, size = %d)", f.name, f.size)
}

type Directory struct {
	name string
	level int
	totFileSize int
	parent *Directory
	subDirs []*Directory
	files []*fileObj
}

type directories []*Directory

func (d *Directory) String() string {
	return fmt.Sprintf("%s (dir, %d)", d.name, d.level)
}


func newFile(name string, size int) *fileObj {
	return &fileObj{name, size}
}

func newDirectory(name string, level int) *Directory {
	tmpDir := &Directory{
		name: name,
		level: level,		
	}
	return tmpDir
}

func (d *Directory) AddSubDir(other *Directory) {
	if (*d).subDirs == nil {
		d.subDirs = make(directories, 0)
	}
	d.subDirs = append(d.subDirs, other)
}

func (d *Directory) hasSubdirs() bool {
	return len(d.subDirs) > 0
}

func (d *Directory) hasFiles() bool {
	return len(d.files) > 0
}

func (d *Directory) hasChildren() bool {
	return d.hasSubdirs() || d.hasFiles()
}

// Move up one directory by name of parent.
func (rootDir *Directory) getParentOf(baseDir *Directory) *Directory {
	return directoryBfs(rootDir, baseDir.parent.name)
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
		if nextDir.hasChildren() {
			for _, subDir := range nextDir.subDirs {
				q = append(q, subDir)
			}
		}
	}
	return nil
}


// DFS
func directoryDfs(baseDir *Directory, name string) *Directory {
	if baseDir.name == name {
		return baseDir
	}

	if baseDir.hasChildren() {
		for _, subDir := range baseDir.subDirs {
			directoryDfs(subDir, name)
		}
	}
	return nil
}

// Sum of file sizes in directory.
func (d *Directory) fileSum() int {
	var tot int
	if d.hasFiles() {
		for _, f := range d.files {
			tot += f.size
		}
	}
	return tot
}

func isDirectory(obj interface{}) bool {
	switch obj.(type) {
	case Directory:
		return true
	default:
		return false
	}
}

// TODO: Fix this
// Walk dirs 
func walkDirsAndSumTotal(d *Directory, maxVal, runningTot int) {
	for _, subDir := range d.subDirs {
		var subTot int
		if subDir.hasFiles() && subDir.totFileSize <= maxVal {
			subTot += subDir.totFileSize
			// printf("%d\n", subDir.totFileSize)
		}
		walkDirsAndSumTotal(subDir, maxVal, runningTot + subTot)
	}
	printf("%d\n", runningTot)
}

// View tree
func viewTree(rootDir *Directory) {
	printf("%s\n", rootDir)

	printlvl := int(rootDir.level+2)
	if rootDir.hasChildren() {
		for _, f := range rootDir.files {
			printf("%*s%s\n", printlvl, " ", f)
		}
		for _, sd := range rootDir.subDirs {
			printf("%*s%s\n", printlvl, " ", sd)
		}		
	}
	if rootDir.hasSubdirs() {
		for _, subDir := range rootDir.subDirs {
			viewTree(subDir)
		}
	}
}


var scanner *bufio.Scanner
var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanws(a ...interface{}) { fmt.Fscan(reader, a...) }
