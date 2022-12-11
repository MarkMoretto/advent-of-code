use std::io::BufReader;
use std::io::prelude::*;
use std::fs::File;
use std::cmp;

const FILE_PATH: &'static str = "./day01/src/data.in";

fn main() -> std::io::Result<()> {
	let f = File::open(FILE_PATH)?;
	let rdr = BufReader::new(f);

	// Alternative to read file.
	// use std::fs;
	// let raw_data = fs::read_to_string(FILE_PATH).expect("error reading file.");
	// let lines: Vec<String> = raw_data.lines().map(String::from).collect();

	// Part 1
	// solve(rdr);

	// Part 2
	solve(rdr);

	Ok(())
}


// part 1 solution
#[allow(dead_code)]
fn solve(brdr: BufReader<File>) -> () {
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