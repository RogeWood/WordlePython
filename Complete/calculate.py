
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

def compareWord(guessString, words):
    if guessString not in words[length]: # 單字不再 list 裡
        print("word not in the list!\n")
    elif guessString == ans: # 正確答案
        print(color[2] + guessString + color[0])
        print("\nAll right!")
        return
    else: # 錯誤單字
        appearedChar = [] # 除存出現過得字母
        for i in range(ord('z')+1):
            appearedChar.append(0)
        for a in ans:
            appearedChar[ord(a)] += 1

        result = [] # 位置結果: 0=>未出現 1=>出現 2=>位置正確
        for i in range(len(guessString)):
            if guessString[i] == ans[i]: # 位置正確
                appearedChar[ord(guessString[i])] -= 1
                result.append(2)
        for i in range(len(guessString)):
            if appearedChar[ord(guessString[i])]: # 字母有出現
                appearedChar[ord(guessString[i])] -= 1
                result.append(1)
            else: # 字母未出現
                result.append(0)
