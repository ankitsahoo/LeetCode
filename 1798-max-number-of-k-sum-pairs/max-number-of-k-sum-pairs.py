from collections import Counter

class Solution:
    def maxOperations(self, nums, k):
        count = Counter(nums) 
        operations = 0
        
        for num in count:
            complement = k - num
            
            if num == complement:
                operations += count[num] // 2  
            elif complement in count:
                pair_count = min(count[num], count[complement])
                operations += pair_count
                count[num] -= pair_count
                count[complement] -= pair_count

        return operations
