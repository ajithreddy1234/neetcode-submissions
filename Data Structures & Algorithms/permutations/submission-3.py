class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cur):
            if cur==len(nums):
                ans.append(nums[:])
                return
            for i in range(cur,len(nums)):
                nums[i],nums[cur]=nums[cur],nums[i]
                backtrack(cur+1)
                nums[i],nums[cur]=nums[cur],nums[i]
        ans=[]
        backtrack(0)
        return ans