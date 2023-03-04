for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    buses = []
    i = 0
    while i < n:
        bus_weight = 0
        for j in range(18):
            if i < n:
                bus_weight += a[i]
                i += 1
            else:
                break
        buses.append(bus_weight)
    if len(buses) > 1 and buses[-1] < 12*18:
        # send another bus to pick up the remaining students
        last_bus_weight = buses.pop()
        for j in range(12):
            if i < n:
                last_bus_weight += a[i]
                i += 1
            else:
                break
        buses.append(last_bus_weight)
    print(min(buses))
