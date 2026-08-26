class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        seen=set(recipes)
        indegree=defaultdict(int)
        adj=defaultdict(list)
        for i in range(len(ingredients)):
            for ele in ingredients[i]:
                adj[ele].append(recipes[i])
                indegree[recipes[i]]+=1
        dq=deque(supplies)
        final=[]
        while dq:
            x=dq.popleft()
            if x in seen:
                final.append(x)
            for nei in adj[x]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    del indegree[nei]
                    dq.append(nei)
        return final
