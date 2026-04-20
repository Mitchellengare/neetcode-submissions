class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l, r = 0, n-1

        while l<r:
            s[l], s[r] = s[r], s[l]

            r-=1
            l+=1