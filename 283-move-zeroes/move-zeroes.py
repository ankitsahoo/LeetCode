from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        right = 0  

        
        for left in range(len(nums)):
            if nums[left] != 0:
                
                nums[right], nums[left] = nums[left], nums[right]
                right += 1


sol = Solution()


nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

# Example 2
nums = [0]
sol.moveZeroes(nums)
print(nums)  # Output: [0]
