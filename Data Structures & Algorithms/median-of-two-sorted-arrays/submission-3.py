class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x=sorted(nums1+nums2)
        return float(x[len(x)//2]) if len(x)%2!=0 else (x[len(x)//2]+x[len(x)//2-1])/2 