class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([])
        self.dfs(0, visited, rooms)
        return len(visited) == len(rooms)

    def dfs(self, node, visited, rooms):
        if node in visited: return
        visited.add(node)
        for nei in rooms[node]:
            self.dfs(nei, visited, rooms)