package main

import (
	d "aoc2021/day1"
	"fmt"
	"os"
	"bufio"
	"strconv"
)

var dataFileName string = "day1.txt"

const dataFolder string = "data"
var FilePath string
var pFilePath *string = &FilePath

func init() {
	*pFilePath = fmt.Sprintf("%s/%s", dataFolder, dataFileName)
}

func getData(output *[]int) {

	file, err := os.Open(FilePath)
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		i, err := strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Println(err)
		}
		*output = append(*output, i)
	}
	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}	
}

func main() {
	var dataMain []int
	getData(&dataMain)
	d.Solution(dataMain)
}
