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

class Button():
    def __init__(self, text, pos, background, parnetSize, size = [200, 75]):
        # 按鈕設定
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
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(x, y):
            print(self.text, "BUTTON DOWN")
            return True
        return False

class Text():
    def __init__(self, text, pos, fontSize, parnetSize, color):
        self.font = pygame.font.Font("font/Roboto-Black.ttf", fontSize)
        self.textSurface = self.font.render(text, True, color)
        self.poistion = Vector2(calculate.middlePosition([parnetSize[0] + pos[0], parnetSize[1] + pos[1]], self.textSurface.get_size()))

class SettingMenu():
    def __init__(self):
        self.backButton = Button("Back", [0, 400], GameSetting.buttonColor, GameSetting.screenSize)

class Menu():
    def __init__(self):
        self.titleText = Text("W o r d l e", [0, 0], 64, GameSetting.screenSize, (255,255,255))
        self.titleText.poistion.y = 30
        self.buttons = {"start": Button("Start", [0, -210], GameSetting.buttonColor, GameSetting.screenSize),
                        "setting": Button("Setting", [0, 10], GameSetting.buttonColor, GameSetting.screenSize),
                        "exit": Button("Exit", [0, 210], GameSetting.buttonColor, GameSetting.screenSize)
                       }
