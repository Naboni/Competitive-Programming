n = int(input())
memo = {1: 1}
def solve(n):
    if n not in memo:
        if n % 2: 
            memo[n] = 1 + solve(n*3+1)
        else: 
            memo[n] = 1 + solve(n//2)
    return memo[n]
print(solve(n))