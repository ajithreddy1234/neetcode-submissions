class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        pivot=l      
        def Bina(l : int,r : int) -> int :
            if  target>nums[r] or target<nums[l]:
                return -1
            while l<r:
                m=(l+r)//2
                if nums[m]<target:
                    l=m+1
                else:
                    r=m
            return l if nums[l]==target else -1
        if Bina(0,pivot-1)==-1:
            return Bina(pivot,len(nums)-1)
        else:
            return Bina(0,pivot-1)

                    


        