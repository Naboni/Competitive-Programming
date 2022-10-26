n = int(input())

def sumOfDigits(num):
    summ = 0
    while num:
        summ += num % 10
        num = num // 10
    return summ 

def solve(num):
    if num < 9:
        return num
    else:
        x = 0
        while x*10+9 <= num:
            x = x*10+9
        return sumOfDigits(x) + sumOfDigits(num-x)

print(solve(n))