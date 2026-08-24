class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = dict() #map from item --> its index

        res = [0] * 2

        for i, num in enumerate(nums):
            if target-num in d:
                return [d[target-num], i]

            d[num] = i