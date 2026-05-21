class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x=nums.copy()
        prod=1
        m=set()
        for num in nums:
            prod=prod*num
        pre=1
        for num in nums:
            if num==0 and num not in m:
                m.add(num)
                continue
            elif num in m:
                pre=0
                break
            pre=pre*num
        
        if prod!=0:
            for i in range(len(x)):
                x[i]=prod//x[i]
        else:
            k=1
            for i in range(len(x)):
                if nums[i]!=0:
                    x[i]=0
                else:
                    x[i]=pre
        return x

        