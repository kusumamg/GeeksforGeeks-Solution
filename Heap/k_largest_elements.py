
import heapq

class Solution:
    def kLargest(self, arr, k):

        heap = []

        for num in arr:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return sorted(heap, reverse=True)