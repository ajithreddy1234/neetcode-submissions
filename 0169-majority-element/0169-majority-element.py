class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter=defaultdict(int)
        for ele in nums:
            counter[ele]+=1
            if counter[ele]>len(nums)//2:
                return ele
        