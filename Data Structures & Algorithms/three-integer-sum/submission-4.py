class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        li=[]
        nums.sort()
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            print(i,l,r)
            while l<r:
                su=nums[i]+nums[l]+nums[r]
                if su==0:
                    print(su)
                    m=[nums[i],nums[l],nums[r]]
                    li.append(m)
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    while nums[r]==nums[r+1] and l<r:
                        r-=1
                elif su<0:
                    l+=1
                else:
                    r-=1
                
        return li