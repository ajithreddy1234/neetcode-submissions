class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        m=n
        stack=[]
        cur_sum=0
        while len(stack)!=m:
            x=k-cur_sum
            value=min(26,x-(n-1))
            stack.append(value)
            cur_sum+=value
            n-=1
        s=""
        for ele in reversed(stack):
            s+=chr(ele-1+ord("a"))
        return s
        