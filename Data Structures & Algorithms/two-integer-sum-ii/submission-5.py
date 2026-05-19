class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l=i+1
            r=len(numbers)-1
            t=target-numbers[i]
            while l<=r:
                mid=(l+r)//2
                if numbers[mid]==t:
                    return [i+1,mid+1]
                elif numbers[mid]>t:
                    r=mid-1
                else:
                    l=mid+1
        return []
                
        