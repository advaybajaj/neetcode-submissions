import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, point in enumerate(points):
            dist = math.sqrt((point[0] ** 2) + (point[1] ** 2))
            pair = (dist, point)
            heapq.heappush(heap, pair)

        res = []
        for _ in range(k):
            pair = heapq.heappop(heap)
            res.append(pair[1])

        return res