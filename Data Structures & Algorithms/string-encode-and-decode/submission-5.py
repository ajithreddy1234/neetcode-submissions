from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded=[]
        for m in strs:
            encoded.append(str(len(m)))
            encoded.append("#")
            encoded.append(m)
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            le=int(s[i:j])
            ele=s[j+1:j+1+le]
            res.append(ele)
            i=int(j+1+le)
        return res


            

        