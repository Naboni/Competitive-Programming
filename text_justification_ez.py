s = input()
arr = [i for i in s]
k = int(input())

# Split the characters into words
def changeCharsToWords(characters):
    words = []
    current_word = ""
    for character in characters:
        if character == " ":
            words.append(current_word)
            current_word = ""
        else:
            current_word += character
    # Add the last word
    words.append(current_word)
    return words

def min_lines(characters, max_width):
    words = changeCharsToWords(characters)
    result = []
    line = [words[0]]
    curr = len(words[0])
    for idx, word in enumerate(words[1:]):
        if curr + len(word) + 1 <= max_width:
            line.append(word)
            curr += len(word) + 1
        else:
            x = " ".join(line)
            result.append(x)
            curr = len(word)
            line = [word]
    x = " ".join(line)
    result.append(x)
    print(len(result))
    for row in result:
        print(row)

min_lines(arr, k)