class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cur):
            if len(cur)==len(nums):
                ans.append(cur[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                cur.append(nums[i])
                backtrack(cur)
                cur.pop()
                used[i]=False
        used=[False]*(len(nums))
        ans=[]
        backtrack([])
        return ans
        