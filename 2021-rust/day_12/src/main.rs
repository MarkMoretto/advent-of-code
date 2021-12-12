
use std::{fs::read_to_string, borrow::Borrow};

// https://doc.rust-lang.org/book/ch10-02-traits.html

// #[derive(Debug)]
// struct Node {
//     value: &'static str,
//     left: &'static Node,
//     right: &'static Node,
// }

pub type NodeIndex = usize;

#[derive(Debug)]
pub struct Node {
    pub value: usize,
    pub left: Option<NodeIndex>,
    pub right: Option<NodeIndex>,
}
impl Node {
    pub fn new(
        value: usize,
        left: Option<NodeIndex>,
        right: Option<NodeIndex>,
    ) -> Self {
        Node { value, left, right }
    }
}

pub struct Tree {
    arena: Vec<Option<Node>>,
    root: Option<NodeIndex>,
}

impl Tree {
    pub fn new() -> Self {
        Tree { 
            arena: Vec::new(),
            root: None
        }
    }

    pub fn iter(&self) -> PreorderIter {
        PreorderIter::new(self.root)
    }

    pub fn set_root(&mut self, root: Option<NodeIndex>) {
        self.root = root;
    }

    pub fn add_node(&mut self, node: Node) -> NodeIndex {
        let idx = self.arena.len();
        self.arena.push(Some(node));
        idx
    }

    pub fn delete_node_at(&mut self, index: NodeIndex) -> Option<Node> {
        if let Some(node) = self.arena.get_mut(index) {
            node.take()
        } else {
            None
        }
    }

    pub fn node_at(&self, index: NodeIndex) -> Option<&Node> {
        return if let Some(node) = self.arena.get(index) {
            node.as_ref()
        } else {
            None
        }
    }

    pub fn node_at_mut(&mut self, index: NodeIndex) -> Option<&mut Node> {
        return if let Some(node) = self.arena.get_mut(index) {
            node.as_mut()
        } else {
            None
        }
    }
}

pub struct PreorderIter {
    stack: Vec<NodeIndex>,
}

impl PreorderIter {
    pub fn new(root: Option<NodeIndex>) -> Self {
        if let Some(node) = root {
            PreorderIter {
                stack: vec![node]
            }
            } else {
                PreorderIter {
                    stack: vec![]
            }
        }
    }

    fn next(&mut self, tree: &Tree) -> Option<NodeIndex> {
        while let Some(node_idx) = self.stack.pop() {
            if let Some(node) = tree.node_at(node_idx) {
                if let Some(right) = node.right {
                    self.stack.push(right)
                }


                if let Some(left) = node.left {
                    self.stack.push(left)
                }
            return Some(node_idx)
        }
    }
        return None
    }    
}




fn get_input(fname: &str) -> String {
    let raw_data = read_to_string(fname).unwrap();
    return raw_data.trim().to_string();
}


fn main() {
    let file_name = "input-sample";
    let mut total = 0;



    // Loop label action
    // https://doc.rust-lang.org/book/ch03-05-control-flow.html
    // 'get_line: for line in get_input(file_name).lines() {
    //     let mut stacker: Vec<char> = Vec::new();
    //     for cc in line.chars() {
    //         match cc {
    //             '(' | '[' | '{' | '<' => stacker.push(cc),
    //             ')' | ']' | '}' | '>' => {
    //                 if stacker.len() == 0 || cc != brace_map(*stacker.last().unwrap()) {
    //                     total += score1(cc);
    //                     continue 'get_line;
    //                 }
    //                 stacker.pop();
    //             }
    //             _ => panic!("Cound not find match for: {}", cc),
    //         }
    //     }
    // }
    println!("Part 1 result: {}", total);
}
