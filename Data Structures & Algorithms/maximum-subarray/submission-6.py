class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        su=0
        res=-float("inf")
        for r in range(len(nums)):
            su+=nums[r]
            if su<0:
                su=0
            else:
                res=max(res,su)

        return res if res!=-float("inf") else max(nums)
            
        