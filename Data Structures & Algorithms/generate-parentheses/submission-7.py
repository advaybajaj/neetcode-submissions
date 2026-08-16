class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(curr, numOpen, numClose):

            if len(curr) == (n * 2):
                res.append(curr)
                return
            if not curr or numOpen < n:
                backtrack(curr + "(", numOpen + 1, numClose)
            if numClose < numOpen and numClose < n:
                backtrack(curr + ")", numOpen, numClose + 1)

        backtrack("", 0, 0)
        return res