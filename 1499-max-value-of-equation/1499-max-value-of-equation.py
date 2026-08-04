class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        x=deque()
        res=-float("inf")
        for r in range(len(points)):
            while x and abs(x[0][0]-points[r][0])>k:
                m=x.popleft()
            if x:
                res=max(res,x[0][1]+points[r][0]+points[r][1])
            while x  and x[-1][1]<points[r][1]-points[r][0]:
                n=x.pop()
            x.append([points[r][0],points[r][1]-points[r][0]])
        return res
        
        