from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        x=set()
        l=0
        res=0
        cur_sum=0
        for r in range(len(nums)):
            while nums[r] in x:
                x.remove(nums[l])
                cur_sum-=nums[l]
                l+=1
            x.add(nums[r])
            cur_sum+=nums[r]
            res=max(res,cur_sum)
        return res

