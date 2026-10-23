class Solution(object):
    def longestPalindrome(self, s):
        ma=""
        for i in range(len(s)):
            if len(ma)<1:
                ma=s[i]
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(ma)<r-l+1:
                    ma=s[l:r+1]
                l-=1
                r+=1
            l=i-1
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(ma)<r-l+1:
                    ma=s[l:r+1]
                l-=1
                r+=1
        return ma

        