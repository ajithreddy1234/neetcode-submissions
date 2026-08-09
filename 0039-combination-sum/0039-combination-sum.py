class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start,cur,total):
            if total==target:
                ans.append(cur[:])
                return
            if total>target:
                return
            for r in range(start,len(candidates)):
                cur.append(candidates[r])
                total+=candidates[r]
                backtrack(r,cur,total)
                x=cur.pop()
                total-=x
        ans=[]
        backtrack(0,[],0)
        return ans