def reverseWordsStr(s: str) -> str:
    words = s.split(" ")
    words = words[-1::-1]
    opstr = ' '.join(words)
    return opstr

print(reverseWordsStr("welcome to python programming"))
    