class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        incoming = defaultdict(int)
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                adj[ingredients[i][j]].append(recipes[i])
                incoming[recipes[i]] += 1
        q = deque()
        for k in supplies:
            q.append(k)
        res = []
        while q:
            node = q.popleft()
            for neigh in adj[node]:
                incoming[neigh] -= 1
                if incoming[neigh] == 0:
                    q.append(neigh)
                    res.append(neigh)
        return res