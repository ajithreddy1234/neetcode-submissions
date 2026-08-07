class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        se={0:1}
        prefix_sum=0
        ams=0
        for r in range(len(nums)):
            prefix_sum+=nums[r]
            target=prefix_sum-goal
            if target in se:
                ams+=se[target]
            if prefix_sum in se:
                se[prefix_sum]+=1
            else:
                se[prefix_sum]=1
        return ams




        