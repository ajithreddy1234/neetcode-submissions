class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i ,num in enumerate(nums):
            a.append([num,i])
        i=0
        a.sort()
        j=len(nums)-1
        while(i<j):
            if a[i][0]+a[j][0]== target:
                return [min(a[i][1],a[j][1]),max(a[i][1],a[j][1])]
            elif a[i][0]+a[j][0]>target :
                j-=1
            else:
                i+=1
        return []

        
        