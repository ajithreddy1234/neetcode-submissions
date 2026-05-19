class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        s=[]
        def df(i):
            if i>=len(nums):
                res.append(s.copy())
                return
            s.append(nums[i])
            df(i+1)
            s.pop()
            df(i+1)
        df(0)
        return res