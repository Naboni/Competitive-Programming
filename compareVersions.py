def compareVersion(version1: str, version2: str) -> int:
    arr1 = version1.split('.')
    arr2 = version2.split('.')
    if len(arr1) != len(arr2):
        while len(arr1) < len(arr2):
            arr1.append('0')
        while len(arr2) < len(arr1):
            arr2.append('0')

    i = j = 0
    while i < len(arr1) and j < len(arr2):
        x, y = int(arr1[i]), int(arr2[j])
        if y == x:
            i += 1
            j += 1
            continue
        elif y > x:
            return -1
        elif y < x:
            return 1
        i += 1
        j += 1
    return 0

version1 = "1.1.0"
version2 = "1.2"
print(compareVersion(version1, version2))