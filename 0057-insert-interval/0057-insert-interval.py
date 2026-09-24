from typing import List

class Solution:
    def insert( self,intervals: List[List[int]],newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        me=[]
        if newInterval[0]<=intervals[0][0]:
            print(1)
            me.append(newInterval)
        for start,end in intervals:
            if me and me[-1][1]>=newInterval[0]:
                me[-1][1]=max(me[-1][1],newInterval[1])
            elif start>newInterval[0]:
                me.append(newInterval)
            if not me or me[-1][1]<start:
                me.append([start,end])
            
            else:
                me[-1][1]=max(me[-1][1],end)
        if me[-1][1]>=newInterval[0]:
            me[-1][1]=max(me[-1][1],newInterval[1])
        elif me[-1][1]<newInterval[0]:
            me.append(newInterval)
        return me