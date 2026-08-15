class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        length = len(nums)
        boolArr = [False] * length

        def backtrack(curr):
            if len(curr) == length:
                res.append(curr.copy())
                return

            for i in range(length):
                if not boolArr[i]:
                    curr.append(nums[i])
                    boolArr[i] = True

                    backtrack(curr)

                    curr.pop()
                    boolArr[i] = False

        backtrack([])
        return res