class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x=set(nums)
        maxx=0

        for num in x:
            if num-1 not in x:
                leng=1
                while num+leng in x:
                    leng+=1
                maxx=max(leng,maxx)
        return maxx




        