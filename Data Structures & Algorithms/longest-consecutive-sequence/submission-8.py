class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=sorted(nums)
        res=1
        m=1
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]:
                continue
            if nums[i+1]==nums[i]+1:
                print(m)
                m+=1
                res=max(res,m)
            else:
                m=1
        return res


