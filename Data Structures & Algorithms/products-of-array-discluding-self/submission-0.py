class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=[]
        for i in range(len(nums)):
            curr = 1
            for j in range(len(nums)-1,-1,-1):
                if i!=j:
                    curr *= nums[j]
            prod.append(curr) 
        return prod

            
        