ctt = int(input())
for ct in range(ctt):
    s = input()

    ev = []
    od = []

    for i in s:
        if int(i)%2 == 0:
            ev.append(int(i))
        else:
            od.append(int(i))

    r = []
    i = 0
    j = 0
    while i < len(ev) and j < len(od):
        if ev[i] < od[j]:
            r.append(ev[i])
            i += 1
        else:
            r.append(od[j])
            j += 1
    for k in range(i, len(ev)):
        r.append(ev[k])
    for k in range(j, len(od)):
        r.append(od[k])

    print(*r, sep="")
