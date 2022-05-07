class Solution:
    def isValid(self, s: str) -> bool:
        char = {'(':')', '{':'}', '[':']'}
        arr = []
        for i in s:
            if i in char.keys():
                arr.append(i)
            elif arr == [] or char[arr.pop()]!=i:
                return False
        if len(arr) == 0:
            return True
        return

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("{[]}"))
