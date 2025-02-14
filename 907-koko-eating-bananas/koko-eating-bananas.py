class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAllBananas(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if canEatAllBananas(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
