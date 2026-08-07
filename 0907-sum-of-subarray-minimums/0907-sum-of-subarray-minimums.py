from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        Mod=10**9+7
        ans=0
        stack=[]
        for i in range(len(arr)+1):
            curr=arr[i] if i<len(arr) else 0
            while stack and arr[stack[-1]]>curr:
                mg=stack.pop()
                l=stack[-1] if stack else -1
                left=mg-l
                right=i-mg
                ans+=(arr[mg]*left*right)
            stack.append(i)
        return ans%Mod