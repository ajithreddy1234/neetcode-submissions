class Solution:
    def maximumSwap(self, num: int) -> int:
        mummy=list(str(num))
        dummy=[-1]*10
        for i in range(len(mummy)):
            dummy[int(mummy[i])]=i
        for i in range(len(mummy)):
            x=int(mummy[i])
            for r in range(9,x,-1):
                if dummy[r]>0 and dummy[r]>i:
                    mummy[i],mummy[dummy[r]]=mummy[dummy[r]],mummy[i]
                    return int("".join(mummy))
        return num



            