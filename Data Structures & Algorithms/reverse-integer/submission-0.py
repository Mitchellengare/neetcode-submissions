class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)

        s = str(x)[::-1]
        reversedInt = int(s) * sign

        if reversedInt <= -2**31 or reversedInt >= 2**31:
            return 0

        return reversedInt