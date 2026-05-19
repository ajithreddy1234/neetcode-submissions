class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=1
        sset=set()
        maxx=0
        for i in range(len(s)):
            while s[i]  in sset:
                sset.remove(s[l])
                l+=1
            sset.add(s[i])
            maxx=max(maxx,i-l+1)
        return maxx
        
                
        