

fn sample_data() -> Vec<u32> {
    vec![16u32, 1, 2, 0, 4, 2, 7, 1, 2, 14]
}

fn main() {
    
    let v = sample_data();
    for x in &v {
        print!("{:?} ", x);
    }
    println!("The sum is: {:?}", vsum(&v));
    println!("The mean is: {:?}", vmean(&v));
}

// fn is_odd(n: u32) -> bool {
//     n % 2 == 1
// }

fn vsum(items: &Vec<u32>) -> u32 {
    let mut output: u32 = 0;
    for i in items {
        output += i;
    }
    return output;
}

fn vmean(items: &Vec<u32>) -> f32 {
    vsum(items) as f32 / items.len() as f32
}