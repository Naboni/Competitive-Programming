t = int(input())
def currentDigitsSum(n):
    sum = 0
    while(n):
        sum += n%10
        n = n // 10
    return sum
for i in range(t):
    n, s = [int(item) for item in input().split()]
    totalMoves = 0
    multiplier = 1
    while(s < currentDigitsSum(n)):
        # / multiplier = number of digits to left , %10 to retrieve the digit itself
        digit = (n // multiplier) % 10
        increment = ((10-digit) % 10) * multiplier
        increment = int(increment)
        n += increment
        multiplier = multiplier * 10 # one digit to left
        totalMoves += increment
    print(totalMoves)
    
t = int(input())
 
# for i in range(t):
#   n, s = [int(j) for j in input().split()]
#   ops = 0
#   mult = 10
 
#   while True:
#     digits = 0
#     n2=n
 
#     digits = sum(int(digit) for digit in str(n))
    
#     if digits <= s:
#       break
    
#     else:
#         lastn = n % mult
#         if lastn != 0:
#             n += mult-lastn
#             ops += mult - lastn
#         mult *= 10
  
#   print (ops)