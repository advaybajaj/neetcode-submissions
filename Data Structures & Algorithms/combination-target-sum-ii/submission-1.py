class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        add = 0

        def backtrack(start, track):
            nonlocal add

            if add == target:
                res.append(track.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if add > target:
                    return

                track.append(candidates[i])
                add += candidates[i]

                backtrack(i+1, track)

                track.pop()
                add -= candidates[i]

        backtrack(0, [])
        return res