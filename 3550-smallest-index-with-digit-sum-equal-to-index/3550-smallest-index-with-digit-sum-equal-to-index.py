class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def check(num):
            s=str(num)
            su=0
            for ele in s:
                su+=int(ele)
            return su
        for i in range(len(nums)):
            if i<10 and i==nums[i]:
                return i
            elif check(nums[i])==i:
                return i
        return -1
        