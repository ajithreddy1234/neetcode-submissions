class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        mg={}
        x=nums2[-1]
        mg[x]=-1
        stack=[]
        stack.append(x)
        for i in range(len(nums2)-2,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            if stack:
                mg[nums2[i]]=stack[-1]
            else:
                mg[nums2[i]]=-1
            stack.append(nums2[i])
        l=[]
        for ele in nums1:
            l.append(mg[ele])
        return l
                

                    