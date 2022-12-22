width = 15
userWidth = 5

# messages = [[1, "Hello how r u"], [2, "good ty"], [2, "u"], [1, "me too bro"]]
# messages = [[1, "Hello how r u"], [2, "good ty"], [2, "u here me"], [1, "me too bro"]]

closers = "+" + "*"*width + "+"
border = "|"
def solve(message):
    side, msg = message
    result = []
    words = msg.split()
    row = [words[0]]
    curr = len(words[0])
    for idx, word in enumerate(words[1:]):
        if curr + len(word) + 1 <= userWidth:
            row.append(word)
            curr += len(word) + 1
        elif curr + len(word) + 1 > userWidth:
            if side == 1:
                aft = " " * (width-curr+1)
                row.append(aft)
            else:
                bef = " " * (width-curr+1)
                row = [bef] + row
            x = " ".join(row)
            result.append("|"+x+"|")
            curr = len(word)
            row = [word]

    if side == 1:
        aft = " " * (width-curr+1)
        row.append(aft)
    else:
        bef = " " * (width-curr+1)
        row = [bef] + row
    x = " ".join(row)
    result.append("|"+x+"|")
    return result

ans = []
ans.append(closers)
for item in messages:
    n = solve(item)
    if not n: continue
    for el in n:
        ans.append(el)
ans.append(closers)
print(ans)

['+***************+', 
'|Hello            |', 
'|how r            |', 
'|u                |', 
'|             good|', 
'|               ty|', 
'|                u|', 
'|me               |', 
'|too              |', 
'|bro              |', 
'+***************+']

['+***************+', 
'|Hello            |', 
'|how r            |', 
'|u                |', 
'|             good|', 
'|               ty|', 
'|                u|', 
'|             here|', 
'|              me|', 
'|me               |', 
'|too              |', 
'|bro              |', 
'+***************+']