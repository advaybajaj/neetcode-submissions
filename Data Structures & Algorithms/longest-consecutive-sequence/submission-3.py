class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxStreak = 0
        streak = 0
        for num in nums:
            if num-1 not in s:
                streak = 0
                x = num
                while x in s:
                    streak += 1
                    maxStreak = max(streak, maxStreak)
                    x += 1
        return maxStreak