class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res=0
        for i in range(len(matrix)):
            if max(matrix[i])<target:
                continue
            else:
                l=0
                r=len(matrix[i])-1
                while l<=r:
                    m=(l+r)//2
                    if matrix[i][m]==target:
                        return True
                    elif matrix[i][m]<target:
                        l=m+1
                    else:
                        r=m-1
                continue
        return False

        