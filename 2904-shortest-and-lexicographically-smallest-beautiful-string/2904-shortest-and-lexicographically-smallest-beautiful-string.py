class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans=""
        ones=0
        l=0
        for r in range(len(s)):
            if s[r]=="1":
                print(r)
                ones+=1
            while ones>k:
                if s[l]=="1":
                    ones-=1
                l+=1
            while l<=r and ones==k and s[l]=="0":
                l+=1
            if ones==k:
                cnadi=s[l:r+1]
                if (ans=="" or len(ans)>len(cnadi) or(len(ans)==len(cnadi) and  ans>cnadi)):
                    ans=cnadi
        return ans
            



        