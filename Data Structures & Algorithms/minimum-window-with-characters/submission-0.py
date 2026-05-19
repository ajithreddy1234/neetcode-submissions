from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t) or t=='':
            return ""
        sT={}
        tT=Counter(t)
        res=[-1,-1]
        reslen=float("inf")
        l=0
        have=0
        need=len(tT)
        for i in range(len(s)):
            sT[s[i]]=sT.get(s[i],0)+1
            if s[i] in tT and sT[s[i]]==tT[s[i]]:
                have+=1
            while have==need:
                if i-l+1 < reslen:
                    res=[l,i]
                    reslen=i-l+1
                sT[s[l]] = sT.get(s[l], 0) - 1

                if s[l] in tT and sT[s[l]] < tT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float("inf") else ""

            
                    

        
            
                
                
                    
                
            
        

            


    
        
        