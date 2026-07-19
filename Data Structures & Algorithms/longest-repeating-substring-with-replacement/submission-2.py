class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res=0
        mp={}
        for r in range(len(s)):
            mp[s[r]]=1+mp.get(s[r],0)
            
            while sum(mp.values())-max(mp.values())>k :
                mp[s[l]]-=1
                if mp[s[l]]==0:
                    del mp[s[l]]
                l+=1
                
            res=max(res,sum(mp.values()))
        return res
                

        