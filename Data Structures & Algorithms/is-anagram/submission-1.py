class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        m={}
        n={}
        for i in range(len(s)):
            m[s[i]]=1+m.get(s[i],0)
            n[t[i]]=1+n.get(t[i],0)
        return m==n