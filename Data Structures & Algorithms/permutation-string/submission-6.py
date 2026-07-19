from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        x=Counter(s1)
        print(x)
        l=0
        r=len(s1)
        mp=Counter(s2[:len(s1)])
        if mp==x:
                return True
        while r<len(s2):
            mp[s2[r]]+=1
            mp[s2[l]]-=1
            if not mp[s2[l-1]]:
                del mp[s2[l-1]]
            if mp==x:
                return True
            print(mp)
            l+=1
            r+=1
        return False
        

        