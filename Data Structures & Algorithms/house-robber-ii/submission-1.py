class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)== 1:
            return nums[0]

        maxR = max(self.robTwo(nums[1:]), self.robTwo(nums[:-1]))
        return maxR

    def robTwo(self, nums):
        prev1 = 0
        prev2 = 0

        for num in nums:
            cur = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = cur

        return prev1

        