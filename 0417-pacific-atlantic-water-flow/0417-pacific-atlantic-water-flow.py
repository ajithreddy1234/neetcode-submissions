class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        def dfs(i,j,cur):
            nonlocal pacific,atlantic
            if i<0 or j<0:
                pacific=True
                return
            if i>rows-1 or j>cols-1:
                atlantic=True  
                return  
            if cur<heights[i][j] or (i,j) in visited:
                return
            if pacific and atlantic:
                return
            visited.add((i,j))
            dfs(i+1,j,heights[i][j])
            dfs(i-1,j,heights[i][j])
            dfs(i,j+1,heights[i][j])
            dfs(i,j-1,heights[i][j])
            return
        final=[]
        for i in range(rows):
            for j in range(cols):
                pacific=False
                atlantic=False
                visited=set()
                dfs(i,j,heights[i][j])
                if pacific and atlantic:
                    final.append([i,j])
        return final


        