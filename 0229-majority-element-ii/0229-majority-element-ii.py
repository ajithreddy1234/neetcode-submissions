class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        x=Counter(nums)
        final=[]
        for key,value in x.items():
            if value>n//3:
                final.append(key)
        return final

        