class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        su=0
        res=-float("inf")
        r=0
        while r<len(nums):
            su+=nums[r]
            if su<=0:
                su=0
                r+=1
            else:
                res=max(res,su)
                print(r,res)
                r+=1
        return res if res!=-float("inf") else max(nums)
            
        