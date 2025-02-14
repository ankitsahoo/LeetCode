class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        prev1, prev2 = 0, 0  
        for money in nums:
            current = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = current
        return prev1
