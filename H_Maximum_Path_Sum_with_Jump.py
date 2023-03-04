import sys, threading
from cmath import inf
from functools import lru_cache

def main():
    @lru_cache(None)
    def dp(node, par):
        summ = values[node-1]
        for child in adj_list[node]:
            if child != par:
                child_sum = dp(child, node)
                summ = max(summ, values[node-1] + child_sum)
        
        ans = -inf
        for child in adj_list[node]:
            if child != par:
                for grand in adj_list[child]:
                    if grand != node:
                        g_sum = dp(grand, child)
                        ans = max(ans, values[node-1] + g_sum)
        
        return max(summ, ans)

    n = int(input())
    values = list(map(int, input().split()))
    adj_list = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    res = -inf
    for i in range(1, n+1):
        res = max(res, dp(i, 0))
    print(res)

threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()