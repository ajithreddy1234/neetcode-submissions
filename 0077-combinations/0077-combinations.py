class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start,curr,ans):
            if len(curr)==k:
                ans.append(curr[:])
                return 
            for i in range(start,n+1):
                curr.append(i)
                backtrack(i+1,curr,ans)
                curr.pop()
        ans=[]
        backtrack(1,[],ans)
        return ans