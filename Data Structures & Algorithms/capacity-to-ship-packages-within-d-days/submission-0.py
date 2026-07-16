class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(m:int):
            day=1
            su=0
            for weigh in weights:
                su+=weigh
                if su>m:
                    day+=1
                    if day>days:
                        return False
                    su=weigh
            return True
        l=max(weights)
        r=sum(weights)
        while l<r:
            m=l+(r-l)//2
            if check(m):
                print(m)
                r=m
            else:
                l=m+1
        return l