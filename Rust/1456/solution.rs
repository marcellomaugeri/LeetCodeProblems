impl Solution {
    pub fn max_vowels(s: String, k: i32) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let (mut left, mut right) = (0 , k as usize);
        let mut current_sum = s.chars().take(k as usize).filter(|character| "aeiou".contains(character.to_ascii_lowercase())).count();
        let mut max_count = current_sum;
        while right < s.len() {
            if "aeiou".contains(chars[left]) {
                current_sum -= 1;
            }
            if "aeiou".contains(chars[right]) {
                current_sum += 1;
            }

            max_count = max_count.max(current_sum);
            right += 1;
            left += 1;
        }
        return max_count as i32;
    }
}