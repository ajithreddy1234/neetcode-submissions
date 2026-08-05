class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        fin=[]
        for l in range(1,len(nums)):
            if nums[l]!=nums[l-1]+1:
                for num in range(nums[l-1]+1,nums[l]):
                    fin.append(num)
        return fin
        