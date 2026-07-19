from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        x=Counter(s1)
        l=0
        r=n-1
        while r<len(s2):
            if Counter(s2[l:r+1])==x:
                return True
            l+=1
            r+=1
        return False
        

        