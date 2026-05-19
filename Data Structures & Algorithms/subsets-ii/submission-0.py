class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        s=[]
        nums.sort()
        def df(i):
            if i>=len(nums):
                res.append(s.copy())
                return 
            s.append(nums[i])
            df(i+1)
            s.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            df(i+1)
        df(0)
        return res

        