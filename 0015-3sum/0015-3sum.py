class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        mg=[]
        print(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                while l<r and l!=i+1 and nums[l]==nums[l-1]:
                    l+=1
                while l<r and r!=len(nums)-1 and nums[r]==nums[r+1]:
                    r-=1
                if l>=r:
                    break
                cal=nums[i]+nums[l]+nums[r]
                if cal==0:
                    mg.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif cal<0:
                    l+=1
                else:
                    r-=1
        return mg


            