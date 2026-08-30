class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mi=min(nums)
        ma=max(nums)
        mi_ind=0
        ma_ind=0
        n=len(nums)
        for i in range(n):
            if nums[i]==mi:
                mi_ind=i
            if nums[i]==ma:
                ma_ind=i
        print(mi,ma,mi_ind,ma_ind)
        return min(max(ma_ind,mi_ind)+1,(n-(abs(ma_ind-mi_ind)-1)),n-min(ma_ind,mi_ind))