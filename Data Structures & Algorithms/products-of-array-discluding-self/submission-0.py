class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros=0
        prod=1
        for num in nums:
            if num:
                prod*=num
            else:
                zeros+=1
        res=[]
        if zeros>1 : return [0]*len(nums)
        for i,val in enumerate(nums):
            if zeros: 
                if val:
                    res.append(0)
                else:
                    res.append(prod)
            else : res.append(prod//val)
        return res

            





