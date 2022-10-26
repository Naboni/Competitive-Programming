tests = int(input())
def main(freq):
    for i in range(10):
        if freq[i] <= 0:
            continue
        freq[i] -=1
        for j in range(i, 10):
            if freq[j] <= 0:
                continue
            freq[j] -= 1
            for k in range(j, 10):
                if freq[k] > 0:
                    if i + j + k in [3,13,23]:
                        # print(i, j, k)
                        return "YES"
            freq[j] +=1
        freq[i] += 1
    return "NO"
for _ in range(tests):
    n = int(input())
    nums = list(map(int, input().split()))
    freq = [0] * 10
    for i in range(n):
        freq[nums[i] % 10] += 1
    print(main(freq))