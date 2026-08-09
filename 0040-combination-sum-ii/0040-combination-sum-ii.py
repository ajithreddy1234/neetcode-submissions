class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(start,cur,total):
            if total==target:
                ans.append(cur[:])
                return
            if total>target:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                cur.append(candidates[i])
                total+=candidates[i]
                backtrack(i+1,cur,total)
                m=cur.pop()
                total-=m
        ans=[]
        backtrack(0,[],0)
        return ans
        