class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        beforePrev = 1

        for _ in range(n-1):
            temp = prev
            prev += beforePrev
            beforePrev = temp
        
        return prev