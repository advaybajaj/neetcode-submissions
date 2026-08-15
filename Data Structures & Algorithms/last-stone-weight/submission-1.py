import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i, num in enumerate(stones):
            heapq.heappush(heap, -num)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first == second:
                continue
            else:
                first -= second
                heapq.heappush(heap, -first)

        if not heap:
            return 0
        return -heap[0]