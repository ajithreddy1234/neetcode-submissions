class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        yes=False
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums)-1,i,-1):
                if nums[j]>nums[i]:
                    print(nums[j],nums[i])
                    yes=True
                    nums[j],nums[i]=nums[i],nums[j]
                    x=[]
                    for k in range(i+1,len(nums)):
                        x.append(nums[k])
                    x.sort()
                    print(x)
                    ll=0
                    for k in range(i+1,len(nums)):
                        nums[k]=x[ll]
                        ll+=1
                    break
            if yes:
                break
        if not yes: 
            nums.sort()
        