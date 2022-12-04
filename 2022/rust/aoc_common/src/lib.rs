
pub fn add_one(n: i32) -> i32 {
	n + 1
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn add_one_success() {
		assert_eq!(10, add_one(9));
	}

	#[test]
	fn add_one_failure() {
		assert_ne!(9, add_one(9));
	}
}
