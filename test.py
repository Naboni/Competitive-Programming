
from cmath import inf


def max_path_sum_with_jump(node, parent, adj_list, values, memo):
    if (node, parent) in memo:
        return memo[(node, parent)]
    
    max_sum = values[node-1]
    for child in adj_list[node]:
        if child != parent:
            child_sum = max_path_sum_with_jump(child, node, adj_list, values, memo)
            max_sum = max(max_sum, values[node-1] + child_sum)
    
    max_jump_sum = -inf
    for child in adj_list[node]:
        if child != parent:
            for grandchild in adj_list[child]:
                if grandchild != node:
                    grandchild_sum = max_path_sum_with_jump(grandchild, child, adj_list, values, memo)
                    max_jump_sum = max(max_jump_sum, values[node-1] + grandchild_sum)
    
    memo[(node, parent)] = max(max_sum, max_jump_sum)
    return memo[(node, parent)]

n = int(input())
values = list(map(int, input().split()))
adj_list = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

max_sum = -inf
for i in range(1, n+1):
    memo = {}
    max_sum = max(max_sum, max_path_sum_with_jump(i, 0, adj_list, values, memo))
print(max_sum)
