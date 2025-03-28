def reverseWords( s: str):


    i = 0
    st = 0
    in_word = False
    out =[]
    while i < len(s):
        if not in_word and s[i] != " ":
            st = i
            in_word = True

        elif in_word and s[i] == " ":
            out.insert(0, s[st:i])
            in_word = False
        elif in_word and i == len(s) -1:
            out.insert(0, s[st:])
        i+=1

    return " ".join(out)

print(reverseWords("a good   example"))