class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[(len(nums)-k)]

        heap = [-s for s in nums]
        heapq.heapify(heap)
        popped = None

        for i in range(k):
            popped = heapq.heappop(heap)

        return -popped

        
        