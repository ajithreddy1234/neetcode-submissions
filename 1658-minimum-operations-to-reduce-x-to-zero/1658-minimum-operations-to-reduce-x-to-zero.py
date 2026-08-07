class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if min(nums)>x:
            return -1
        res=-float("inf")
        ioo=sum(nums)
        if ioo<x:
            return -1
        if ioo==x:
            return len(nums)
        su=ioo-x
        l=0
        cur=0
        for r in range(len(nums)):
            cur+=nums[r]
            while cur>su and l<=r:
                print(cur)
                cur-=nums[l]
                l+=1
            if cur==su:
                print(1)
                res=max(res,r-l+1)
        print(res,len(nums),ioo)
        
        return len(nums)-res if res!=-float("inf") else -1

            

        


        
        