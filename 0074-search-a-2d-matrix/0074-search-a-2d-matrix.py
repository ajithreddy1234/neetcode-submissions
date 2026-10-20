class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def binary(i):
            x=matrix[i]
            l=0
            r=len(x)-1
            while l<=r:
                mid=(l+r)//2
                if x[mid]==target:
                    return True
                elif x[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
          
            return False
        rows=len(matrix)
        cols=len(matrix[0])
        i=0
        j=rows-1 
        check=float("inf")
        while i<=j:
            mid=(i+j)//2
            if matrix[mid][cols-1]>=target:
                check=min(check,mid)
                j=mid-1
            else:
                i=mid+1
        return binary(check) if check!=float("inf") else False
        