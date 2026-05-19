class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            coun=[0]*26
            for c in s:
                coun[ord(c)-ord('a')]+=1
            res[tuple(coun)].append(s)
        return list(res.values())
        
       
            

        