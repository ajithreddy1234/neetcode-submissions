class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre={i:[] for i in range(numCourses)}
        for i,l in prerequisites:
            pre[i].append(l)
        res=[]
        visit=set()
        x=set()
        def dfs(c):
            if c in visit:
                return False
            if c in x:
                return True
            visit.add(c)
            for p in pre[c]:
                if dfs(p)==False:
                    return False
            x.add(c)
            visit.remove(c)
            res.append(c)
            pre[c]=[]
            return True
        for c in range(numCourses):
            if  dfs(c)==False:
                return []

        return res


        