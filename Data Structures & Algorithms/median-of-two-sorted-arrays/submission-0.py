class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sort=[]
        l=0
        r=0
        while l<len(nums1) and r<len(nums2):
            if nums1[l]<nums2[r]:
                sort.append(nums1[l])
                l+=1
            else:
                sort.append(nums2[r])
                r+=1
        while l<len(nums1):
            sort.append(nums1[l])
            l+=1
        while r<len(nums2):
            sort.append(nums2[r])
            r+=1
        print(sort)
        


        
        l=0
        r=len(sort)-1
        m=(l+r)/2
        if int(m)!=m:
            k=int(m)
            x=sort[k+1]
            y=sort[k]
            return (x+y)/2
        else:
            return sort[int(m)]

        