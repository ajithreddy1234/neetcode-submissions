class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        m=n
        s=""
        cur_sum=0
        while len(s)!=m:
            x=k-cur_sum
            value=min(26,x-(n-1))
            s+=chr(value-1+ord("a"))
            cur_sum+=value
            n-=1
        return s[::-1]
        