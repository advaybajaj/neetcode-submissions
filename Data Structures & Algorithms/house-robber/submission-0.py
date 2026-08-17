class Solution:
    def rob(self, nums: List[int]) -> int:
        d = {}
        def dp(i):
            if i >= len(nums) or i < 0:
                return 0
            if i in d:
                return d[i]
            d[i] = max(nums[i] + dp(i+2), dp(i+1))
            return d[i]

        return dp(0)