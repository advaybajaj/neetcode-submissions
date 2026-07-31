class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        mid = 0
        while (l<=r):
            mid = (l+r) // 2
            if(self.timeToFinishAllPiles(piles, mid) > h):
                l = mid + 1
            elif(self.timeToFinishAllPiles(piles, mid) <= h):
                r = mid - 1
        return l

    def timeToFinishAllPiles(self, piles: List[int], k: int) -> int:
        sumHours = 0
        for num in piles:
            sumHours += math.ceil(num / k)
        return int(sumHours)
