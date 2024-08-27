import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kheap = []
        for num in nums:
            if len(kheap) < k:
                heapq.heappush(kheap, num)
            elif num > kheap[0]:
                heapq.heappop(kheap)
                heapq.heappush(kheap, num)
        return kheap[0]