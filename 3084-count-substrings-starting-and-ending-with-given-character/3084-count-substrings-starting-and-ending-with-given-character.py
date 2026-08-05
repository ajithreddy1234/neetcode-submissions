class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        x=Counter(s)
        c=x[c]
        return (c*(c+1))//2
        