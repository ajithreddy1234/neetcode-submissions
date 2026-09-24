class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        me=[]
        for i in range(len(intervals)):
            if not me or me[-1][1]<intervals[i][0]:
                me.append(intervals[i])
            else:
                me[-1][1]=max(me[-1][1],intervals[i][1])
        return me
        