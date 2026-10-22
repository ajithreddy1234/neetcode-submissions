class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def palindrome(st):
            l=0
            r=len(st)-1
            while l<r:
                if st[l]!=st[r]:
                    return False
                l+=1
                r-=1
            return True
        res=[]
        def backtrack(i,li):
            print(li)
            for ch in range(i,len(s)):
                if not palindrome(s[i:ch+1]):
                    continue
                if ch==len(s)-1:
                    li.append(s[i:ch+1])
                    res.append(li[:])
                    li.pop()
                li.append(s[i:ch+1])
                backtrack(ch+1,li)
                li.pop()
        backtrack(0,[])
        return res
        

        