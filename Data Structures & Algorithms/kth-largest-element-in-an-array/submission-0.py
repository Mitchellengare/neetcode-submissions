class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [-s for s in nums]
        # heapq.heapify(nums)

        # while 
        nums.sort()
        return nums[(len(nums)-k)]
        