class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        overlaps = 0
        i = 0

        while i < len(intervals)-1:
            curr = intervals[i]
            nxt = intervals[i+1]
            if curr[1] > nxt[0]:
                overlaps += 1
                if curr[1] > nxt[1]:
                    intervals.pop(i)
                else:
                    intervals.pop(i+1)
            else:
                i += 1

        return overlaps