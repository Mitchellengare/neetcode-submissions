"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals or len(intervals) == 1:
            return True

        intervals.sort(key=lambda interval: interval.start)

        for r in range(1, len(intervals)):
            if intervals[r].start <  intervals[r-1].end:
                return False

        return True