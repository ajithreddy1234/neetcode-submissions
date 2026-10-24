class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def check(i):
            for j in range(len(needle)):
                if i>=len(haystack):
                    return False
                if haystack[i]!=needle[j]:
                    return False
                if j==len(needle)-1:
                    return True
                i+=1
            return True
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                if check(i):
                    return i
        return -1
            
        