class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, rem, track):
            if rem == 0:
                res.append(track.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > rem:
                    return

                track.append(candidates[i])
                backtrack(i+1, rem-candidates[i], track)
                track.pop()

        backtrack(0, target, [])
        return res