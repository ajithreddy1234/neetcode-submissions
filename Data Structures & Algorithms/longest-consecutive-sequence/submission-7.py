class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=sorted(nums)
        reason=False
        res=1
        for i in range(len(nums)-1):
            if reason==False:
                m=1
            if nums[i+1]==nums[i]:
                continue
            if nums[i+1]==nums[i]+1:
                print(m)
                reason=True
                m+=1
                res=max(res,m)
            else:
                reason=False
        return res


