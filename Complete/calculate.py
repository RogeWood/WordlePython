
def middlePosition(sizeA, sizeB):
    return ((sizeA[0]-sizeB[0])/2, (sizeA[1]-sizeB[1])/2)

def wordDictionary():
    words = []
    with open("word.txt") as f: # 讀單字庫檔
        data = list(f.read().split())
    for w in data: # 將單字長度分類
        while len(words) <= len(w):
            a = []
            words.append(a)
        words[len(w)].append(w)

    return words

def compareWord(guessString, ans, words, length):
    if guessString not in words[length]: # 單字不再 list 裡
        print("word not in the list!\n")
        return [-1]
    if guessString == ans: # 正確答案
        result = []
        for s in guessString:
            result.append(2)
        return result
    else: # 錯誤單字
        appearedChar = [] # 除存出現過得字母
        for i in range(ord('z')+1):
            appearedChar.append(0)

        result = [] # 位置結果: 0=>未出現 1=>出現 2=>位置正確
        usedWord = []
        for i in range(len(guessString)):
            usedWord.append(0)
            appearedChar[ord(ans[i])] += 1

            if guessString[i] == ans[i]: # 位置正確
                appearedChar[ord(guessString[i])] -= 1
                usedWord[i] = 1

        for i in range(len(guessString)):
            if usedWord[i]:
                result.append(2)
            else:
                if appearedChar[ord(guessString[i])]: # 字母有出現
                    appearedChar[ord(guessString[i])] -= 1
                    result.append(1)
                else: # 字母未出現
                    result.append(0)
        return result

def resultCheck(result):
    for i in result:
        if i != 2:
            return False
    return True
