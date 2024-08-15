impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let chars: Vec<char> = s.chars().filter(|c| c.is_alphanumeric()).collect(); // filter out non-alphanumeric characters and convert to vector
        let (mut left, mut right) = (0, chars.len() - 1); // init the two pointers

        if chars.is_empty(){ // if the string (without non-alphanumeric characters) is empty, return true as required
            return true;
        }

        while left < right { // loop until the two pointers meet
            if chars[left].to_ascii_lowercase() != chars[right].to_ascii_lowercase() { // if we find a mismatch, return false
                return false;
            }
            left += 1;
            right -= 1;
        }
        true // if we reach here, the string is a palindrome for sure
    }
}