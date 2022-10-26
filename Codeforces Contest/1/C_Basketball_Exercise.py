from functools import lru_cache
n = int(input())
first = list(map(int, input().split()))
sec = list(map(int, input().split()))

@lru_cache
def top_down(index, isOne):
    if index >= n:
        return 0
    if isOne:
        choose_first = first[index] + top_down(index+1, False)
        choose_none = top_down(index+1, True)
        choose_none2 = top_down(index+1, False)
        return max(choose_first, choose_none, choose_none2)
    else:
        choose_sec = sec[index] + top_down(index+1, True)
        choose_none = top_down(index+1, True)
        choose_none2 = top_down(index+1, False)
        return max(choose_sec, choose_none, choose_none2)

print(max(top_down(0, True), top_down(0, False)))