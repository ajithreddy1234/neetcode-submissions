class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=sorted(nums)
        print(nums)
        g_val=1
        l_val=1
        for i in range(len(nums)-1):
            if nums[i+1]==(nums[i]+1):
                if i==len(nums)-1:
                    l_val+=1
                print(nums[i])
                l_val+=1
                g_val=max(g_val,l_val)
                print(l_val,g_val)
            elif nums[i+1]==nums[i]:
                continue
            else:
                l_val=1
                g_val=max(g_val,l_val)
        return g_val


