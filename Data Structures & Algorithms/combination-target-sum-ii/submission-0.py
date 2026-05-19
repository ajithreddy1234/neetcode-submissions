class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=set()
        candidates.sort()
        def df(i,cur,total):
            if total==target:
                res.add(tuple(cur))
                return
            elif total>target or i>=len(candidates):
                return 
            cur.append(candidates[i])
            df(i+1,cur,total+candidates[i])
            cur.pop()
            df(i+1,cur,total)
            

        df(0,[],0)

        return [list(c) for c in res]
         
        