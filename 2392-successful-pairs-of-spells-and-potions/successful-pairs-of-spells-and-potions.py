class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        
        for spell in spells:
            left, right = 0, len(potions) - 1
            count = 0
            
            # Binary search to find the first potion that will make the pair successful
            while left <= right:
                mid = left + (right - left) // 2
                if spell * potions[mid] >= success:
                    count = len(potions) - mid
                    right = mid - 1
                else:
                    left = mid + 1
                    
            result.append(count)
        
        return result
