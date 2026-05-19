class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        x=[]
        nums.sort()
        for i in range(n):
            r=n-1
            l=i+1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                summ=nums[i]+nums[r]+nums[l]
                if summ==0:
                    x.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif summ>0:
                    r-=1
                else:
                    l+=1
        return x
                

                        
        
        
                        