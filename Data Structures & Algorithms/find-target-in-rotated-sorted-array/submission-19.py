class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=l +(r-l)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        pivot=l
        k=0
        m=len(nums)-1
        if target >= nums[pivot] and target <=nums[m]:
            k=pivot
        else:
            m=pivot-1
        while k<=m:
            mid=k+(m-k)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                m=mid-1
            else:
                k=mid+1
        return -1
        

            

