import pygame
import calculate
from pygame.math import Vector2

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
    faildTimes = 5

    # 遊戲狀態
    running = True
    gameOver = True
    setting = False

class Button():
    def __init__(self, text, pos, background, parnetSize, size = [200, 75], parnetPos = Vector2(0,0)):
        # 按鈕設定
        self.mouseDivide = parnetPos
        self.poistion = Vector2(calculate.middlePosition([parnetSize[0] + pos[0], parnetSize[1] + pos[1]], size))
        self.fontSize = 24
        self.size = size
        self.text = Text(text, [0, 0], self.fontSize, self.size, pygame.Color("Black"))

        # 按鈕建制
        self.surface = pygame.Surface(size)
        self.surface.fill(background)
        self.surface.blit(self.text.textSurface, calculate.middlePosition(size, self.text.textSurface.get_size()))
        self.rect = pygame.Rect(self.poistion.x, self.poistion.y, size[0], size[1])

    def click(self, event): # 按下按鈕
        x, y = Vector2(pygame.mouse.get_pos()) - self.mouseDivide
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(x, y):
            print(self.text, "BUTTON DOWN")
            return True
        return False

class Text():
    def __init__(self, text, pos, fontSize, parnetSize, color):
        self.font = pygame.font.Font("font/Roboto-Black.ttf", fontSize)
        self.textSurface = self.font.render(text, True, color)
        self.color = color
        self.poistion = Vector2(calculate.middlePosition([parnetSize[0] + pos[0], parnetSize[1] + pos[1]], self.textSurface.get_size()))

    def textChange(self, text):
        self.textSurface = self.font.render(text, True, self.color)

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
        self.valueText.textChange(str(text))
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
