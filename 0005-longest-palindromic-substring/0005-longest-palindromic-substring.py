class Solution(object):
    def longestPalindrome(self, s):
        if len(s)<=1:
            return s
        n=len(s)
        def check(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        mg=""
        for i in range(len(s)):
            if len(mg)<1:
                mg=s[i]
            j=n-1
            while i<j:
                if s[i]==s[j]:
                    if j-i+1>len(mg):
                        if check(i,j):
                            mg=s[i:j+1]
                            break
                j-=1
        return mg
            
                
                        





        