class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        mg=image[sr][sc]
        def dfs(i,j):
            if i<0 or j<0 or i>len(image)-1 or j>len(image[0])-1 or image[i][j]!=mg or image[i][j]==color:
                return
            image[i][j]=color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return
        dfs(sr,sc)
        print(image)
        return image
