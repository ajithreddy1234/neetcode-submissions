class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        co1={}
        n1=len(s1)
        n2=len(s2)
        for i in range(n1):
            co1[s1[i]]=1+co1.get(s1[i],0)
        for i in range(n2-n1+1):
            co2=Counter(s2[i:i+n1])
            if co2==co1:
                return True
            
                
                
        return False



        