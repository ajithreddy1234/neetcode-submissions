class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(li):
            if len(nums)==len(li):
                res.append(li[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                li.append(nums[i])
                backtrack(li)
                li.pop()
                used[i]=False
        used=[False]*len(nums)
        res=[]
        backtrack([])
        return res

        