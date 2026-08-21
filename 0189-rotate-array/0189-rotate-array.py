class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        k=k%n
        x=nums[-k:]+nums[:n-k]
        print(x)
        for i in range(len(nums)):
            nums[i]=x[i]