from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        x=defaultdict(int)
        l=0
        res=0
        cur_sum=0
        for r in range(len(nums)):
            while x[nums[r]]:
                x[nums[l]]-=1
                cur_sum-=nums[l]
                l+=1
            x[nums[r]]=1
            cur_sum+=nums[r]
            res=max(res,cur_sum)
        return res

