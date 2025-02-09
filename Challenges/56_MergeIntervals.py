class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        index = 0
        start, end = 0, 1
        for i in range(len(intervals)):
            if i==0:
                continue
            prev, cur = intervals[index], intervals[i]
            if prev[start] <= cur[start] <= prev[end] or prev[start] <= cur[end] <= prev[end]:
                prev[start] = min(prev[start], cur[start])
                prev[end] = max(prev[end], cur[end])
            else:
                index += 1
                intervals[index][0] = cur[start]
                intervals[index][1] = cur[end]    
        return intervals[:index+1]
