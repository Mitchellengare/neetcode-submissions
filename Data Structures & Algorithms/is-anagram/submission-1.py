class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ss = sorted(s)
        tt = sorted(t)

        for i in range (len(s)):
            if ss != tt:
                return False
        return True
        