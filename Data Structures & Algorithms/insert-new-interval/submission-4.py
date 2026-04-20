class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1
        intervals.insert(i, newInterval)

        i = 0
        while i < len(intervals) - 1:
            curr = intervals[i]
            nxt  = intervals[i + 1]
            if curr[1] >= nxt[0]:  
                curr[1] = max(curr[1], nxt[1])  
                intervals.pop(i + 1)            
            else:
                i += 1

        return intervals