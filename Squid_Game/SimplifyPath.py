class Solution:
    def simplifyPath(self, path):
        stack = []
        sett = set([".", "", ".."])
        directory = path.split("/")
        for i in range(len(directory)):
            if stack and directory[i] == "..":
                stack.pop()
            elif directory[i] not in sett:
                stack.append(directory[i])
        res = "/".join(stack)
        return "/" + res