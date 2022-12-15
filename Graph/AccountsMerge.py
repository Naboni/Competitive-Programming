class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parent = {}
        rank = {}
        def find(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 1
            if parent[x] == x:
                return x
            return find(parent[x])

        def union(x, y):
            fx, fy = find(x), find(y)
            if fx == fy: return
            if rank[fx] >= rank[fy]:
                parent[fy] = fx
                rank[fx] += rank[fy]
            else:
                parent[fx] = fy
                rank[fy] += rank[fx]

        users = {}
        for i in range(len(accounts)):
            for j in accounts[i][1:]:
                if j not in users:
                    users[j] = i
                else:
                    union(users[j], i)
        result = defaultdict(list)
        for email, user in users.items():
            par = find(user)
            result[par].append(email)
        ans = []
        for i in result:
            x = [accounts[i][0]]
            x.extend(sorted(result[i]))
            ans.append(x)
        return ans