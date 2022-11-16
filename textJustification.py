class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        x = len(words[0])
        res = []
        row = [words[0]]
        for i in range(1, len(words)):
            x += len(words[i]) + 1
            if x > maxWidth:
                res.append(row)
                x = len(words[i])
                row = []
            row.append(words[i])
        k = 0
        for i in res:
            k += len(i)
        res.append(words[k:])
        print(res)
        ans = []
        for row in res[:-1]:
            tot = 0
            for w in row:
                tot += len(w)
            lvl = []
            i = 0
            if len(row) == 1:
                lvl.append(row[0])
                space = maxWidth - len(row[0])
                lvl.append(" "*space)
                ans.append("".join(lvl))
                continue
            v = maxWidth - tot
            x = v//(len(row)-1)
            mod = v % (len(row)-1)
            while i < len(row)-1:
                lvl.append(row[i])                
                lvl.append(" "*x)
                if mod > 0:
                    lvl.append(" ")
                    mod -= 1
                i += 1
            lvl.append(row[i])
            ans.append("".join(lvl))
        lvl = []
        tot = 0
        for r in res[-1]:
            tot += len(r)
            lvl.append(r)
        x = [" ".join(lvl)]
        x.append(" "*(maxWidth-tot-(len(res[-1])-1)))
        ans.append("".join(x))
        return ans
            