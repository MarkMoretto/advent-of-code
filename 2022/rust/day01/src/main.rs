use std::io::BufReader;
use std::io::prelude::*;
use std::fs::File;
use std::cmp;

// const FILE_PATH: &'static str = "./day01/src/data-sm.in";
const FILE_PATH: &'static str = "./day01/src/data.in";

fn main() -> std::io::Result<()> {
	let f = File::open(FILE_PATH)?;
	let rdr = BufReader::new(f);

	// Part 1
	// part1(rdr);

	// Part 2
	part2(rdr);

	Ok(())
}

// part 1 solution
#[allow(dead_code)]
fn part1(brdr: BufReader<File>) -> () {
	let mut mx: i32 = -1;
	let mut sub_tot: i32 = 0;
	
	for line in brdr.lines() {
		let curr_line = line.unwrap();
		if curr_line.len() == 0 {
			mx = cmp::max(mx, sub_tot);
			sub_tot = 0;
			continue;
		}
		let n = curr_line.parse::<i32>().unwrap();
		sub_tot += n;
	}
	println!("{mx:?}");
}

// Part 2 solution.
#[allow(dead_code)]
fn part2(brdr: BufReader<File>) -> () {
	// Max capacity for vector.
	const MAX_CAPACITY: usize = 1e6 as usize;

	// Create vector with max capacity in mind.
	let mut elves: Vec<i32> = Vec::with_capacity(MAX_CAPACITY);

	// Mutable variables for sub total and final calorie count
	// of top three elves.
	let mut sub_tot: i32 = 0;
	let mut final_calories: i32= 0;
	
	for line in brdr.lines() {
		let curr_line = line.unwrap();
		if curr_line.len() == 0 {
			// Push all subtotals onto vector.
			// Note: there's probably a more-efficient way to do this,
			// but this works for now.
			elves.push(sub_tot);
			sub_tot = 0;
			continue;
		}
		let n = curr_line.parse::<i32>().unwrap();
		sub_tot += n;
	}

	// Attempt a reverse sort.
	elves.sort_unstable_by(|a, b| b.partial_cmp(a).unwrap());

	// Get top three results.
	let top_three = &elves[0..3];
	for elf in top_three {
		final_calories += elf;	
	}
	println!("{final_calories:?}");
}