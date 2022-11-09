class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.result = []
        self.helper(0, [], s)
        return self.result

    def helper(self, ind, path, s):
        if ind >= len(s):
            self.result.append("".join(path))
            return
        if s[ind].isalpha():
            if s[ind].islower():
                char = s[ind].upper()
            else:
                char = s[ind].lower()
            self.helper(ind+1, path + [char], s)
            self.helper(ind+1, path + [s[ind]], s)
        else:
            self.helper(ind+1, path+[s[ind]], s)