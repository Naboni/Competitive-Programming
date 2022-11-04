n = int(input())

def sieveOfEratoshenes():
    isPrime = [True for _ in range(n+1)]

    p = 2
    while p * p <= n:
        if isPrime[p]:
            for i in range(p * p, n+1, p):
                isPrime[i] = False
        p += 1

    return isPrime

print(sieveOfEratoshenes())