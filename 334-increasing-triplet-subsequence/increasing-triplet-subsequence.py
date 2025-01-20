class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        n = len(nums)
        left_min = [float('inf')] * n
        right_max = [float('-inf')] * n
        left_min[0] = nums[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i-1], nums[i])
        right_max[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i])
        for j in range(1, n-1):
            if left_min[j-1] < nums[j] < right_max[j+1]:
                return True
        return False
