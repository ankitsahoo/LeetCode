class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(c: str) -> bool:
            return c in 'aeiou'
        current_vowels = sum(1 for i in range(k) if is_vowel(s[i]))
        max_vowels = current_vowels
        
        for i in range(k, len(s)):
            if is_vowel(s[i - k]):
                current_vowels -= 1
            if is_vowel(s[i]):
                current_vowels += 1
            max_vowels = max(max_vowels, current_vowels)
        
        return max_vowels
