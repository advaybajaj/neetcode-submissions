class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numToFreq = dict()

        for num in nums:
            numToFreq[num] = numToFreq.get(num, 0) + 1


        buckets = [[] for i in range(len(nums)+1)]
        for num, freq in numToFreq.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            for item in buckets[i]:
                res.append(item)
                k -= 1
                if k == 0:
                    return res