class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        totalWater = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if height[left] <= height[right]:
                totalWater += (min(leftMax, rightMax) - height[left])
                left+=1
            else:
                totalWater += (min(leftMax, rightMax) - height[right])
                right-=1
        
        return totalWater
            