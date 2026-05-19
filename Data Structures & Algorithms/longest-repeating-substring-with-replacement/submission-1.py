class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        l=0
        maxf=0
        c={}
        for i in range(len(s)):
            c[s[i]]=1+c.get(s[i],0)
            maxf=max(maxf,c[s[i]])
            while (i-l+1)-maxf >k:
                c[s[l]]-=1
                l+=1
            res=max(res,i-l+1)
        return res

        