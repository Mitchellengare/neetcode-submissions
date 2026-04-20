class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1
        s = set(nums)
        while missing in s:
                missing += 1
        return missing