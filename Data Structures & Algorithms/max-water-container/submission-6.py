class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxSoFar = 0

        l = 0
        r = len(heights)-1

        while l<r:
            area = (r-l) * min(heights[l], heights[r])
            maxSoFar = max(maxSoFar, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxSoFar