class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        dic={"0":0,"1":0}
        l=0
        res=0
        opt_l=0
        opt_r=len(s)-1
        entered=False
        for r in range(len(s)):
            dic[s[r]]+=1
            while dic["1"]>=k:
                if dic["1"]==k:
                    entered=True
                    if r-l+1<opt_r-opt_l+1:
                        opt_l=l
                        opt_r=r
                    elif r-l+1==opt_r-opt_l+1:
                        if s[opt_l:opt_r+1]>s[l:r+1]:
                            opt_l=l
                            opt_r=r
                dic[s[l]]-=1
                l+=1
        
        return s[opt_l:opt_r+1] if entered else ""


        