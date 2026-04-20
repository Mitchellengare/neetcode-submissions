class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        l, n = 0, len(nums)

        for r in range(n):
            if nums[r] == 1:
                count += 1
            else:
                count = 0
            maxCount = max(maxCount, count)

        return maxCount