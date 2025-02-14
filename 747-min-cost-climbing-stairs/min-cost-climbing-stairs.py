class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = cost[0], cost[1]
        for i in range(2, len(cost)):
            new_cost = min(prev, curr) + cost[i]
            prev, curr = curr, new_cost
        return min(prev, curr)
