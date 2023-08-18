def getIndex(char):
    return charList.index(char)

def removeSpace(text):
    return text.replace(" ","")

def addSpace(text1,text2):
    text1 = list(text1)
    for i,char in enumerate(text2):
        if char == " ":
            text1.insert(i, " ")
    return "".join(text1)

def encrypt(raw,key):
    txt = removeSpace(raw)
    result = ""
    key += txt
    for i, char in enumerate(txt):
        if char not in charList or key[i] not in charList:
            tempchar = char
        else:
            tempchar = charList[(getIndex(char) + getIndex(key[i])) % 93]
        result += tempchar
    result = addSpace(result,raw)
    return result

def decrypt(raw,key):
    txt = removeSpace(raw)
    keylen = len(key)
    result = ""
    for i, char in enumerate(txt[:keylen]):
        if char not in charList or key[i] not in charList:
            tempchar = char
        else:
            if getIndex(char) < getIndex(key[i]):
                tempchar = charList[93 + getIndex(char) - getIndex(key[i])]
            else:
                tempchar = charList[getIndex(char) - getIndex(key[i])]
        result += tempchar
    key = result
    for i, char in enumerate(txt[keylen:]):
        if char not in charList or key[i] not in charList:
            tempchar = char
        else:
            if getIndex(char) < getIndex(key[i]):
                tempchar = charList[93 + getIndex(char) - getIndex(key[i])]
            else:
                tempchar = charList[getIndex(char) - getIndex(key[i])]
        key += tempchar
        result += tempchar
    result = addSpace(result,raw)
    return result

charList = [chr(i) for i in range(32, 125)]