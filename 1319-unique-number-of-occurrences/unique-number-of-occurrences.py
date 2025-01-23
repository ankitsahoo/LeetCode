from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        freq_set = set()
        for count in counts.values():
            if count in freq_set:
                return False
            freq_set.add(count)
        return True
