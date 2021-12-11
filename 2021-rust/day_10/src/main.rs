
// use std::io::{self, Read};
use std::fs::read_to_string;

// fn get_io_input() -> String {
//     let mut raw_data = String::new();
//     io::stdin().lock().read_to_string(&mut raw_data).unwrap();
//     return raw_data.trim().to_string();
// }

fn get_input(fname: &str) -> String {
    let raw_data = read_to_string(fname).unwrap();
    return raw_data.trim().to_string();
}

fn score1(c: char) -> i64 {
    match c {
        ')' => 3,
        ']' => 57,
        '}' => 1197,
        '>' => 25137,
        _ => panic!("Cound not find match for: {}", c),
    }
}

fn brace_map(c: char) -> char {
    match c {
        '(' => ')',
        '[' => ']',
        '{' => '}',
        '<' => '>',
        _ => panic!("Cound not find match for: {}", c),
    }
}

fn main() {
    let file_name = "input";
    let mut total = 0;
    // Loop label action
    // https://doc.rust-lang.org/book/ch03-05-control-flow.html
    'get_line: for line in get_input(file_name).lines() {
        let mut stacker: Vec<char> = Vec::new();
        for cc in line.chars() {
            match cc {
                '(' | '[' | '{' | '<' => stacker.push(cc),
                ')' | ']' | '}' | '>' => {
                    if stacker.len() == 0 || cc != brace_map(*stacker.last().unwrap()) {
                        total += score1(cc);
                        continue 'get_line;
                    }
                    stacker.pop();
                }
                _ => panic!("Cound not find match for: {}", cc),
            }
        }
    }
    println!("Part 1 result: {}", total);
}

// fn opening_brackets() -> &'static[char] {
//     &['(', '[', '{', '<']
// }

// fn closing_brackets() -> &'static[char] {
//     &[')', ']', '}', '>']
// }