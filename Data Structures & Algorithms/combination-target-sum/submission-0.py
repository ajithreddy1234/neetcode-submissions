class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def df(i,curr,total):
            if total==target:
                res.append(curr.copy())
                return
            if total>target or i>=len(nums):
                return
            curr.append(nums[i])
            df(i,curr,total+nums[i])
            curr.pop()
            df(i+1,curr,total)
        df(0,[],0)
        return res
        