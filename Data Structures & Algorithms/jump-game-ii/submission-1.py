class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        farthest=0
        count=0
        cur_end=0
        n=len(nums)
        for r in range(n):
            farthest=max(farthest,r+nums[r])
            if r==cur_end:
                cur_end=farthest
                count+=1
                if cur_end>=n-1:
                    return count
        