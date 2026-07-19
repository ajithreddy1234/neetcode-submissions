from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s11,s22=[0]*26,[0]*26
        for i in range(len(s1)):
            s11[ord(s1[i])-ord("a")]+=1
            s22[ord(s2[i])-ord("a")]+=1
        matches=0
        for i in range(26):
            matches+=(1 if s11[i]==s22[i] else 0)
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            indi=ord(s2[r])-ord("a")
            s22[indi]+=1
            if s11[indi]==s22[indi]:
                matches+=1
            elif s11[indi]+1==s22[indi]:
                matches-=1
            indi2=ord(s2[l])-ord("a")
            s22[indi2]-=1
            if s11[indi2]==s22[indi2]:
                matches+=1
            elif s11[indi2]-1==s22[indi2]:
                matches-=1 
            l+=1
        return matches==26

        

        