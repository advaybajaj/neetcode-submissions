class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        store = "()" * n

        def backtrack(curr, numOpen, numClose):

            if len(curr) == len(store):
                res.append(curr)
                return

            if numOpen < n:
                backtrack(curr + "(", numOpen + 1, numClose)
            
            if numClose < numOpen:
                backtrack(curr + ")", numOpen, numClose + 1)

        backtrack("", 0, 0)
        return res