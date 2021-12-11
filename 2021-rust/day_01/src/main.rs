
// use std::cmp::Ordering;
// use std::fs;
use std::env;
use std::path::Path;
fn main() {
    let fpath = Path::new("data/sample-input.txt");
    let parent_fpath = fpath.parent();
    let cwd = env::current_dir();
    println!("{:?}", cwd);
    println!("File path: {:?}\nParent: {:?}", fpath.display(), parent_fpath);

    // let input = fs::read_to_string("../data/sample-input.txt").unwrap();
    // let data = parse_input(&input);
    // for n in &data {
    //     println!("{}", n);
    // }
}


// fn parse_input(input_string: &str) -> Vec<u32> {
//     input_string.lines().filter_map(|q| q.parse().ok()).collect()
// }