class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res=[]
        def backtrack(index,state,su):
            if su==target:
                res.append(state[:])
            for choice in range(index,len(candidates)):
                if su+candidates[choice]>target:
                    continue
                state.append(candidates[choice])
                backtrack(choice,state,su+candidates[choice])
                state.pop()

        backtrack(0,[],0)
        return res
        