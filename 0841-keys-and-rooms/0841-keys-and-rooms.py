class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True
        visit=set()
        visited=0
        def dfs(room):
            nonlocal visited
            if room in visit:
                return
            visited+=1
            visit.add(room)
            for nei in rooms[room]:
                dfs(nei)
        dfs(0)
        return visited==len(rooms)