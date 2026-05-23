class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(num):
            if num.isalpha() or num.isdigit():
                return True
        l=0
        r=len(s)-1
        while l<r:
            if not check(s[l]):
                l+=1
            elif not check(s[r]):
                r-=1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                print(s[l],s[r])
                l+=1
                r-=1
        return True
        