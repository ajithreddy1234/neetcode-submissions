class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows=len(triangle)
        for i in range(1,rows):
            print(triangle[i])
            for j in range(len(triangle[i])):
                if j==len(triangle[i])-1:
                    triangle[i][j]+=triangle[i-1][j-1]
                elif j-1>=0:
                    if triangle[i-1][j-1]<triangle[i-1][j]:
                        triangle[i][j]+=triangle[i-1][j-1]
                    else:
                        triangle[i][j]+=triangle[i-1][j]
                else:
                    triangle[i][j]+=triangle[i-1][j]
        print(triangle)
        return min(triangle[-1])


        