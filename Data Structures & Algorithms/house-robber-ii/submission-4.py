class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robLinear(arr):
            d = {}
            def dp(i):
                if i >= len(arr) or i < 0:
                    return 0
                if i in d:
                    return d[i]
                d[i] = max(arr[i] + dp(i+2), dp(i+1))
                return d[i]

            return dp(0)

        if len(nums) == 1:
            return nums[0]

        return max(robLinear(nums[1:]), robLinear(nums[:-1]))