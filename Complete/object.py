import pygame
import calculate
from pygame.math import Vector2
from random import randint

class GameSetting():
    # 視窗設定
    screenHighth = 600
    screenWidth = 1000
    screenSize = [screenWidth, screenHighth]
    screenDefultSize = (screenWidth, screenHighth)
    screenDefultColor = (0, 0, 0)

    # 畫面每秒更新律
    FPS = 60

    # 按鈕顏色
    buttonColor = (250, 250, 210)

    # 遊戲設定
    wordLength = 5
    faildTimes = 6

    # 遊戲狀態
    running = True
    gameOver = True
    setting = False

    # 單字題庫
    wordsDict = calculate.wordDictionary()

class Button():
    def __init__(self, text, pos, background, parnetSize, size = [200, 75], parnetPos = Vector2(0,0)):
        # 按鈕設定
        self.mouseDivide = parnetPos
        self.poistion = Vector2(calculate.middlePosition([parnetSize[0] + pos[0], parnetSize[1] + pos[1]], size))
        self.fontSize = 24
        self.size = size
        self.text = Text(text, [0, 0], self.fontSize, self.size, pygame.Color("Black"))
        self.background = background

        # 按鈕建制
        self.surface = pygame.Surface(size)
        self.surface.fill(self.background)
        self.surface.blit(self.text.textSurface, calculate.middlePosition(size, self.text.textSurface.get_size()))
        self.rect = pygame.Rect(self.poistion.x, self.poistion.y, size[0], size[1])

    def click(self, event): # 按下按鈕
        x, y = Vector2(pygame.mouse.get_pos()) - self.mouseDivide
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(x, y):
            print(self.text, "BUTTON DOWN")
            return True
        return False

    def changeText(self, text): # 更改按鈕文字
        self.surface.fill(self.background)
        self.text.textChange(text)
        self.surface.blit(self.text.textSurface, calculate.middlePosition(self.size, self.text.textSurface.get_size()))

class Text():
    def __init__(self, text, pos, fontSize, parnetSize, color):
        self.font = pygame.font.Font("font/Roboto-Black.ttf", fontSize)
        self.textSurface = self.font.render(text, True, color)
        self.color = color
        self.poistion = Vector2(calculate.middlePosition([parnetSize[0] + pos[0], parnetSize[1] + pos[1]], self.textSurface.get_size()))
        self.parnetSize = parnetSize
        self.pos = pos

    def textChange(self, text): # 更改文字
        self.textSurface = self.font.render(text, True, self.color)
        self.poistion = Vector2(calculate.middlePosition([self.parnetSize[0] + self.pos[0], self.parnetSize[1] + self.pos[1]], self.textSurface.get_size()))

class ValueSetBar():
    def __init__(self, text, pos, background, parnetSize, size = [500, 50]):
        # 變數設定 bar
        self.background = background
        self.surface = pygame.Surface(size)
        self.surfaceSize = size
        self.poistion = Vector2(calculate.middlePosition([parnetSize[0] + pos[0], parnetSize[1] + pos[1]], self.surfaceSize))
        # 文字設定
        self.name = Text(text, [-200, 0], 24, self.surfaceSize, pygame.Color("Black"))
        self.valueText = Text("1", [100, 0], 24, self.surfaceSize, pygame.Color("Black"))
        # 調整按鈕
        self.upButton = Button("+", [160, 0], pygame.Color("Yellow"), self.surfaceSize,[30,30], self.poistion)
        self.downButton = Button("-", [40, 0], pygame.Color("Yellow"), self.surfaceSize,[30,30], self.poistion)

    def update(self, text):
        self.valueText.textChange(str(text)) # 數字顯示調整
        # bar 圖案建制
        self.surface.fill(self.background)
        self.surface.blit(self.name.textSurface, self.name.poistion)
        self.surface.blit(self.upButton.surface, self.upButton.poistion)
        self.surface.blit(self.downButton.surface, self.downButton.poistion)
        self.surface.blit(self.valueText.textSurface, self.valueText.poistion)

class SettingMenu():
    def __init__(self):
        # 設定選單
        self.tableSize = [600,350]
        self.tablePos = Vector2(calculate.middlePosition(GameSetting.screenSize, self.tableSize))

        self.tableSurface = pygame.Surface(self.tableSize)
        self.tableSurface.fill((100, 100, 100))

        # 單字長度
        self.lengthBar = ValueSetBar("Word Length", [0,-100], pygame.Color("Gray"), GameSetting.screenSize)
        self.timesBar = ValueSetBar("Failed Times", [0,100], pygame.Color("Gray"), GameSetting.screenSize)
        # 返回鍵
        self.backButton = Button("Back", [0, 450], GameSetting.buttonColor, GameSetting.screenSize)

    def update(self, screen): # 畫面更新
        self.lengthBar.update(GameSetting.wordLength)
        self.timesBar.update(GameSetting.faildTimes)
        screen.blit(self.tableSurface, self.tablePos)
        screen.blit(self.backButton.surface, self.backButton.poistion)
        screen.blit(self.lengthBar.surface, self.lengthBar.poistion)
        screen.blit(self.timesBar.surface, self.timesBar.poistion)

class Menu():
    def __init__(self):
        # 標題
        self.titleText = Text("W o r d l e", [0, 0], 64, GameSetting.screenSize, (255,255,255))
        self.titleText.poistion.y = 50

        # 選項按鈕
        self.buttons = {"start": Button("Start", [0, -170], GameSetting.buttonColor, GameSetting.screenSize),
                        "setting": Button("Setting", [0, 30], GameSetting.buttonColor, GameSetting.screenSize),
                        "exit": Button("Exit", [0, 230], GameSetting.buttonColor, GameSetting.screenSize)
                       }

    def update(self, screen): # 畫面更新
        for btn in self.buttons:# 按鈕更新
            screen.blit(self.buttons[btn].surface, self.buttons[btn].poistion)
        screen.blit(self.titleText.textSurface, self.titleText.poistion)

class WordBox():
    def __init__(self, pos, size, fontSize, parnetSize, parnetPos):
        # 文字匡面板
        self.size = [size, size]
        self.surface = pygame.Surface(self.size)
        self.poistion = pos
        self.boxColor = pygame.Color("Black")
        self.surface.fill(self.boxColor)

        # 字母設定
        self.alpha = ""
        self.text = Text(self.alpha, pos, fontSize, self.size, pygame.Color("White"))
        self.surface.blit(self.text.textSurface, calculate.middlePosition(self.size, self.text.textSurface.get_size()))

    def update(self, parnetSurface): # 畫面更新
        self.surface.fill(self.boxColor)
        self.surface.blit(self.text.textSurface, calculate.middlePosition(self.size, self.text.textSurface.get_size()))
        parnetSurface.blit(self.surface, self.poistion)

    def changeText(self, alpha): # 更改字母
        self.alpha = alpha
        self.text.textChange(alpha)

class WordTable():
    def __init__(self, pos = [0, 0], boxSize = 60, gap = 10):
        # 單字table
        self.size = [GameSetting.wordLength*(boxSize+gap)+gap, GameSetting.faildTimes*(boxSize+gap)+gap]
        self.surface = pygame.Surface(self.size)
        self.poistion = Vector2(calculate.middlePosition([GameSetting.screenSize[0] - pos[0], GameSetting.screenSize[1] - pos[1]], self.size))
        self.surface.fill((30,30,30))

        #文字方塊
        self.words = []
        for i in range(GameSetting.faildTimes):
            a = []
            for j in range(GameSetting.wordLength):
                a.append(WordBox([gap + (boxSize + gap) * j, gap + (boxSize + gap) * i], boxSize, 24, self.size, self.poistion))
            self.words.append(a)

    def update(self, screen):
        # 文字方塊更新
        for row in self.words:
            for w in row:
                w.update(self.surface)
        screen.blit(self.surface, self.poistion)

    def changeWordBoxColor(self, line, result): # 更改文字匡顏色
        for i in range(GameSetting.wordLength):
            if result[i] == 2: # 位置正確
                self.words[line][i].boxColor = (83, 141, 78)
            elif result[i] == 1: # 有出現
                self.words[line][i].boxColor = (181, 148, 59)
            else: # 未出現
                self.words[line][i].boxColor = (58, 58, 60)

class Game():
    def __init__(self):
        # 遊戲狀態
        self.showAnswer = False
        self.isComplete = False
        self.hintEnable = False
        # 選項按鈕
        self.buttons = {"back": Button("Back to menu", [-800, -170], GameSetting.buttonColor, GameSetting.screenSize),
                        "restart": Button("Restart", [-800, 30], GameSetting.buttonColor, GameSetting.screenSize),
                        "answer": Button("Show answer", [-800, 230], GameSetting.buttonColor, GameSetting.screenSize)
                       }

        # 單字table
        self.wordTable = WordTable()
        self.point = [0, 0]

        # 答案單字
        self.answer = GameSetting.wordsDict[GameSetting.wordLength][randint(1, len(GameSetting.wordsDict[GameSetting.wordLength-1]))]
        print(self.answer)

        # 提示文字
        self.hintText = Text("", [0,-500], 24, GameSetting.screenSize, pygame.Color("White"))

    def update(self, screen): # 畫面更新
        if self.showAnswer:
            self.buttons["answer"].changeText(self.answer)
        else:
            self.buttons["answer"].changeText("Show answer")

        for btn in self.buttons:# 按鈕更新
            screen.blit(self.buttons[btn].surface, self.buttons[btn].poistion)
        self.wordTable.update(screen) # 單字table更新

        if self.hintEnable:
            screen.blit(self.hintText.textSurface, self.hintText.poistion)

    def addAlpha(self, text): # 新增字母
        if self.point[1] < GameSetting.wordLength:
            self.wordTable.words[self.point[0]][self.point[1]].changeText(text)
            self.point[1] += 1

    def deleteAplha(self): # 刪除字母
        if self.point[1] >= 0:
            if self.point[1] > 0:
                self.point[1] -= 1
            self.wordTable.words[self.point[0]][self.point[1]].changeText("")

    def checkWord(self):

        if self.wordTable.words[self.point[0]][GameSetting.wordLength-1].alpha != "": # 最後一個單字
            # 檢查單字
            guessString = ""
            for w in self.wordTable.words[self.point[0]]:
                guessString += w.alpha
            result = calculate.compareWord(guessString, self.answer, GameSetting.wordsDict, GameSetting.wordLength)

            # 單字未出現在字典裡
            if result == [-1]:
                self.hintEnable = True
                self.hintText.textChange("word not in the list!")
                return

            # 更改文字匡顏色
            self.wordTable.changeWordBoxColor(self.point[0], result)

            # 結果檢查
            print(result)
            if calculate.resultCheck(result): # 全對
                self.hintEnable = True
                self.hintText.textChange("All Correct")
                self.isComplete = True
                return

            if self.point[0] == GameSetting.faildTimes-1: # 次數用盡
                self.hintEnable = True
                self.hintText.textChange("game over!!")
                self.isComplete = True
            else: # 移至下一行
                self.point[0] += 1
                self.point[1] = 0
        return
