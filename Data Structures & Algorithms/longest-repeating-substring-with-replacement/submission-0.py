class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        for i in range(len(s)):
            maxf=0
            c={}
            for j in range(i,len(s)):
                c[s[j]]=1+c.get(s[j],0)
                maxf=max(maxf,c[s[j]])
                if k>=(j-i+1)-maxf:
                    res=max(res,j-i+1)
        return res

        