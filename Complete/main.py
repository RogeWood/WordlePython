import pygame
from pygame.locals import *
import object
import calculate

def init():
    # 初始設定
    pygame.init() # 模組初始化
    global screen
    screen = pygame.display.set_mode(object.GameSetting.screenDefultSize) # 視窗變數
    global fpsclock
    fpsclock = pygame.time.Clock() # 畫面更新律變數

    global running
    running = True
    global gameOver
    gameOver = True
    global setting
    setting = False

    # 菜單設定
    global menuObject
    menuObject = object.Menu()

    # 設定菜單設定
    global settingMenuObject
    settingMenuObject = object.SettingMenu()

def menu(event):
    global running
    global gameOver
    global setting

    for btn in menuObject.buttons:
        # 事件處理
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menuObject.buttons[btn].click(event):
                print(btn)
                if btn == "exit": # 結束遊戲
                    running = False
                elif btn == "start":
                    gameOver = False
                elif btn == "setting":
                    setting = True
        # 物件更新
        for btn in menuObject.buttons:# 按鈕更新
            screen.blit(menuObject.buttons[btn].surface, menuObject.buttons[btn].poistion)
        screen.blit(menuObject.titleText.textSurface, menuObject.titleText.poistion)

def settingMenu(event):
    global setting
    # 事件處理
    if event.type == pygame.MOUSEBUTTONDOWN:
        if settingMenuObject.backButton.click(event):
            setting = False
    # 物件更新
    # screen.blit(titleText.textSurface, settingMenuObject.titleText)
    screen.blit(settingMenuObject.backButton.surface, settingMenuObject.backButton.poistion)

def game(event):
    pass

def main():
    # 初始設定
    init()
    global running

    while running: # 程式運行中
        for event in pygame.event.get(): # 讀取事件
            if event.type == pygame.QUIT: # 退出遊戲
                running = False
            else:
                screen.fill((0,0,0)) # 背景色
                if gameOver: # 遊戲結束
                    if setting: # 設定菜單
                        settingMenu(event)
                    else: # 主菜單
                        menu(event)
                else:
                    game(event)

        pygame.display.update()
        fpsclock.tick(object.GameSetting.FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
