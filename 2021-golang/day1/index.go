package day1

/* Advent of Code: Day 1
See: https://adventofcode.com/2021/day/1
*/
import "fmt"

// const testData = []int{199, 200, 208, 210, 200, 207, 240, 269, 260, 263}

// Struct to hold Depth items and info.
type Depths struct {
	items []int 		// List of depth values
	netIncrease int		// Value to hold net increase count acorss all depth values.
}

// Return size of Depths instance.
// return {int} number of elements in Depths instance.
func (d *Depths) Size() int {
	return len(d.items)
}

// Add item to Depths instance.
// parameter {int} item - Integer value to append to list.
func (d *Depths) Add(item int) {
	d.items = append(d.items, item)
}


func (d *Depths) AddAll(depths []int) {
	for i := range depths {
		d.Add(depths[i])
	}
}

func (d *Depths) NIncreased() {
	var i int = 1
	d.netIncrease = 0

	for i < d.Size() {
		if d.items[i]-d.items[i-1] > 0 {
			d.netIncrease++
		}
		i++
	}
}

func Solution(d []int) {
	// var data = []int{199, 200, 208, 210, 200, 207, 240, 269, 260, 263}
	depths := &Depths{}
	depths.AddAll(d)
	depths.NIncreased()
	fmt.Printf("Total count was: %d\n", depths.netIncrease)
}
