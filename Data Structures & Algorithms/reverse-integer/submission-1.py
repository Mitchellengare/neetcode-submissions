class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)

        s = str(x)[::-1]
        res = int(s) * sign

        if res <= -2**31 or res >= 2**31:
            return 0

        return res