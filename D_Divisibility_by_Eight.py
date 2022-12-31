n = input()

def isDivisible(num, div):
    return num % div == 0
num = "00" + n

for i in range(len(num)):
    for j in range(i+1, len(num)):
        for k in range(j+1, len(num)):
            new_num = int(num[i] + num[j] + num[k])
            if isDivisible(new_num, 8):
                print("YES")
                print(new_num)
                exit()
print("NO")
