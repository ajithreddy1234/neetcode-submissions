class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res=[]
        def backtrack(index,state,su):
            if su==target:
                res.append(state[:])
            for choice in range(index,len(candidates)):
                if choice>index and candidates[choice]==candidates[choice-1]:
                    continue
                if su+candidates[choice]>target:
                    continue
                state.append(candidates[choice])
                backtrack(choice+1,state,su+candidates[choice])
                state.pop()

        backtrack(0,[],0)
        return res
        