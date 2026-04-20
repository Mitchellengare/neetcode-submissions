class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        n = len(nums3)
        
        if n == 1:
            return float(nums3[0])

        l, r = 0, n-1
        med = 0.0
        
        while l < r:
            if n%2 == 0: #even array
                r = (n+1)//2
                l = r-1
                med = (nums3[l]+nums3[r])/2
                break

            else: #odd arrray
                r = n//2
                med = (nums3[r])
                break


        return med