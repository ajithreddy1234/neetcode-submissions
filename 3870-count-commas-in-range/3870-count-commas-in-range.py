class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        s=""
        print("9"*3)
        st=str(n)
        count=len(st)
        while count>3:
            s=s+3*"9"
            count-=3
        return n-int(s)
