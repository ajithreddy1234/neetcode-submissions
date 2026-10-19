class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        i=0
        k=len(matrix)-1
        while (i<k):
            for l in range(k-i):
                matrix[i+l][i],matrix[k][i+l]=matrix[k][i+l],matrix[i+l][i]
            print(matrix)
            for l in range(k-i):
                matrix[k][i+l],matrix[k-l][k]=matrix[k-l][k],matrix[k][i+l]
            print(matrix)
            for l in range(k-i):
                matrix[k-l][k],matrix[i][k-l]=matrix[i][k-l],matrix[k-l][k]
                print(matrix[k-l][k],matrix[i][k-l])
            print(matrix)
            i+=1
            k-=1
        
        