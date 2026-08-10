class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def valid(peice):
            return peice==peice[::-1]
        def backtrack(start,path):
            if start==len(s):
                ans.append(path[:])
                return
            for end in range(start,len(s)):
                peice=s[start:end+1]
                if valid(peice):
                    path.append(peice)
                    backtrack(end+1,path)
                    path.pop()
        backtrack(0,[])
        return ans
        