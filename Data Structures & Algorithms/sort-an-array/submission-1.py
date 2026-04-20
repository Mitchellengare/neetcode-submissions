class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # return nums

        # n = len(nums)
        # l, r = 0, n-1

        heapq.heapify(nums)
        res = []

        while nums:
            res.append(heapq.heappop(nums))
        return res

            