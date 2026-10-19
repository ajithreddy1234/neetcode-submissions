class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        x=[]
        for i in range(len(intervals)):
            if x and x[-1][1]>=intervals[i][0]:
                x[-1][1]=max(intervals[i][1],x[-1][1])
            else:
                x.append(intervals[i])
        return x
        