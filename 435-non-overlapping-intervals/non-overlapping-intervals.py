class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        total_length = len(intervals)
        intervals = sorted(intervals, key = lambda x : x[1])
        for interval in intervals:
            if not res or res[-1][1] <= interval[0]:
                res.append(interval)
        return total_length - len(res)
        