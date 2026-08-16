class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def checkPalindrome(s):
            left = 0
            right = len(s)-1

            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        
        res = []

        def backtrack(curr, start):
            
            if start == len(s):
                res.append(curr[:])
                return
            
            for i in range(start, len(s)):

                substring = s[start : i+1]
                if checkPalindrome(substring):
                    curr.append(substring)
                    
                    backtrack(curr, i+1)

                    curr.pop()
        
        backtrack([], 0)
        return res