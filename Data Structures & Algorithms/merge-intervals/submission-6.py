class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0

        while i < len(intervals)-1:
            curr = intervals[i]
            nxt = intervals[i+1]
            if curr[1] >= nxt[0]:
                intervals[i] = [min(curr[0], nxt[0]), max(curr[1], nxt[1])]
                intervals.pop(i+1)
            else:
                i+=1

        return intervals

