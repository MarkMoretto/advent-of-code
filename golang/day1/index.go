package day1

// https://adventofcode.com/2021/day/1
import "fmt"

// const testData = []int{199, 200, 208, 210, 200, 207, 240, 269, 260, 263}

type Depths struct {
	items []int
	netIncrease int
}


func (d *Depths) Size() int {
	return len(d.items)
}

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
