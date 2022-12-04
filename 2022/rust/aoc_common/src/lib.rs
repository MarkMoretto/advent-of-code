use std::io::{self, BufRead};
use std::fs::File;
use std::path::Path;

// Read file line-by-line.
// Returns Reader Iterator for lines of file.
// See: https://doc.rust-lang.org/std/keyword.where.html
#[allow(dead_code)]
pub fn read_lines<Q>(filepath: Q) -> io::Result<io::Lines<io::BufReader<File>>>
where Q: AsRef<Path>, {
	let file = File::open(filepath)?;
	Ok(io::BufReader::new(file).lines())
}



// -- Demo section

// fn main() {

    // // File hosts must exist in current path before this produces output

    // if let Ok(lines) = read_lines("./hosts") {
    //     // Consumes the iterator, returns an (Optional) String
    //     for line in lines {
    //         if let Ok(ip) = line {
    //             println!("{}", ip);
    //         }
    //     }
    // }

    // let input = fs::read_to_string("../data/sample-input.txt").unwrap();
    // let data = parse_input(&input);
    // for n in &data {
    //     println!("{}", n);
    // }

// }


#[allow(dead_code)]
fn file_exists() -> bool {
	true
}

#[allow(dead_code)]
fn parse_input(input_string: &str) -> Vec<u32> {
    input_string.lines().filter_map(|q| q.parse().ok()).collect()
}





// pub fn add_one(n: i32) -> i32 {
// 	n + 1
// }

// #[cfg(test)]
// mod tests {
// 	use super::*;

// 	#[test]
// 	fn add_one_success() {
// 		assert_eq!(10, add_one(9));
// 	}

// 	#[test]
// 	fn add_one_failure() {
// 		assert_ne!(9, add_one(9));
// 	}
// }
