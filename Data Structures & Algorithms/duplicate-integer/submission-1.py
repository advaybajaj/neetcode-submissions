class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        s = set()

        for i, num in enumerate(nums):
            if num in s:
                return True

            s.add(num)
        
        return False