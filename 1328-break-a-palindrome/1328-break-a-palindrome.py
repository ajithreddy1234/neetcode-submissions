class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n=len(palindrome)
        if n==1:
            return ""
        mg=list(palindrome)
        for i in range(n):
            if n%2!=0 and i==n//2:
                continue
            if mg[i]>"a":
                mg[i]="a"
                return "".join(mg)
        mg[-1]="b"
        return "".join(mg)
        