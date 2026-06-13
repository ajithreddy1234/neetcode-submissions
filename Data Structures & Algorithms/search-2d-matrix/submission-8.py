class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t_i=0
        for i in range(len(matrix)):
            if matrix[i][len(matrix[0])-1]>=target:
                t_i=i
                break
        l=0
        r=len(matrix[0])-1
        while l<=r:
            mid=l+(r-l)//2
            if matrix[t_i][mid]==target:
                return True
            elif matrix[t_i][mid]<target:
                l=mid+1
            else:
                r=mid-1
        return False

        

