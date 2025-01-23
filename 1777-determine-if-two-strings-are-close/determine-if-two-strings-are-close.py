class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if sorted(set(word1)) != sorted(set(word2)):
            return False
        return sorted([word1.count(c) for c in set(word1)]) == sorted([word2.count(c) for c in set(word2)])