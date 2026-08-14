class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        add = 0
        length = len(nums)
        def backtrack(start):
            nonlocal add

            if add == target:
                res.append(track.copy())
                return

            if add > target:
                return
            
            for i in range(start, length):
                track.append(nums[i])
                add += nums[i]

                backtrack(i)

                track.pop()
                add -= nums[i]

        backtrack(0)
        return res