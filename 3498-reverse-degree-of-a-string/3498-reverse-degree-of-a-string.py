class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        for i in range(len(s)):
            total+=(ord("z")-ord(s[i])+1)*(i+1)
            print(total)
        return total
        