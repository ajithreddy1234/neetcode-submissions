class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        m=''
        for i in s:
            i=i.lower()
            if "a"<=i<="z" or '0' <= i <= '9':
                m+=i
        for k in range(len(m)):
            if m[k]!=m[len(m)-k-1]:
                return False
        return True

        

        