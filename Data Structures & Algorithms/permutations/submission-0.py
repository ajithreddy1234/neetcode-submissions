class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=[[]]
        for num in nums:
            new=[]
            for p in perms:
                for i in range(len(p)+1):
                    pp=p.copy()
                    pp.insert(i,num)
                    new.append(pp)
            perms=new
        return perms
        