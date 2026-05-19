class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        x=[[]]
        for num in nums:
            s=[]
            for i in x:
                s.append(i+[num])
            x.extend(s)
        return x

        