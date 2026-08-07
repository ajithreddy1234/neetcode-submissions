class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=float("inf")
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                l=i+1
                r=len(nums)-1
                while l<r:
                    tt=nums[i]+nums[l]+nums[r]
                    if abs(tt-target)<abs(res-target):
                        res=tt
                    if tt==target:
                        return target
                    elif tt>target:
                        r-=1
                    else:
                        l+=1
                print(i,l,r)
        return res


