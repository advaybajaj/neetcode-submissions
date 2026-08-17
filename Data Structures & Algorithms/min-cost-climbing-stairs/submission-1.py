class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        d = {}

        def dp(i):
            if i>=len(cost):
                return 0
            if i in d:
                return d[i]
            d[i] = cost[i] + min(dp(i+1), dp(i+2))
            return d[i]

        return min(dp(0), dp(1))