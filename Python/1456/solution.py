class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = k
        maxCount = currentSum = sum(1 for character in s[left:right] if character.lower() in ('a', 'e', 'i', 'o', 'u'))
        while right < len(s):
            if s[left].lower() in ('a', 'e', 'i', 'o', 'u'):
                currentSum -= 1
            if s[right].lower() in ('a', 'e', 'i', 'o', 'u'):
                currentSum += 1
            left += 1
            right += 1
            maxCount = max(maxCount, currentSum)
        return maxCount