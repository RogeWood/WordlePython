from random import randint

words = [] # 單字庫
length = 5 # 單字長度
times = 5 # 失敗次數

color = ['\033[0m', '\033[93m', '\033[92m'] # 顏色 0:defult, 1:yellow, 2:green
def game():
    global times
    global length
    global words
    # 設定答案
    ans = words[length][randint(1, len(words[length])-1)]
    print("The ans is: " + ans)

    # 開始猜測
    while times:
        print("Input word(rest times:", times,") : ")
        guessString = input() # 輸入猜測單字

        if len(ans) == len(guessString): # 長度正確
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
                #輸出猜測結果
                for i in range(len(guessString)):
                    print(color[result[i]] + guessString[i], end='')
                print(color[0])
                times -= 1
        else:
            print("\nwrang word length!")

    print("\nFaill!!")
    return

def gameSetting():
    global times
    global length
    global words

    print("\n- length: adjust word length\n- times: adjust failed times\n- exit: exit game setting")
    while True:
        print("Input setting command: ")
        commandString = input() # 輸入指令字串

        if commandString == "length": # 調整題目長度
            length = int(input(f'- word length is {length}: '))
        elif commandString == "times": # 調整失敗容許次數
            times = int(input(f'- failed times is {times}: '))
        elif commandString == "exit": # 退出設定
            print("\nsetting complete")
            print("word length: ", length)
            print("failed times: ", times)
            return
        else: # 輸入不合法指令
            print("command not found")

    return

def init():
    # 建立單字庫
    with open("word.txt") as f: # 讀單字庫檔
        data = list(f.read().split())
    for w in data: # 將單字長度分類
        while len(words) <= len(w):
            a = []
            words.append(a)
        words[len(w)].append(w)
    return


def main():
    # 遊戲初始化
    init()

    # 遊戲開始
    while True:
        print("Input command: ")
        commandString = input() # 輸入指令字串

        if commandString == "exit": # 退出遊戲
            return
        elif commandString == "help": # 指令教學
            with open("command.txt") as f:
                print(f.read())
        elif commandString == "play": # 遊戲開始
            game()
        elif commandString == "setting": # 遊戲設定
            gameSetting()
        else:
            print("command not found")
            print("type help to see command")
    return

if __name__ == '__main__':
    main()
