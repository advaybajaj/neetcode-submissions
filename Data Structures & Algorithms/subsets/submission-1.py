class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(curr, arr):
            nonlocal res

            if not arr:
                res.append(curr.copy())
                return

            backtrack(curr, arr[1:])

            curr.append(arr[0])
            backtrack(curr, arr[1:])

            curr.pop()

        backtrack([], nums)

        return res
        