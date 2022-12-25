
s = input()
t = input()

sorted_s = sorted(s)
sorted_t = sorted(t)
 
def is_subset(a, b):
    i = 0
    for letter in b:
        if letter == a[i]:
            i += 1
        if i == len(a):
            break
    return i == len(a)
 
 
if sorted_s == sorted_t:
    print('array')
elif is_subset(t, s):
    print('automaton')
elif is_subset(sorted_t, sorted_s):
    print('both')
else:
    print('need tree')