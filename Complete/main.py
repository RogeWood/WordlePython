import pygame
from pygame.locals import *
import object

def init():
    # 初始設定
    pygame.init() # 模組初始化
    global screen
    screen = pygame.display.set_mode(object.GameSetting.screenDefultSize) # 視窗變數
    global fpsclock
    fpsclock = pygame.time.Clock() # 畫面更新律變數

    # 菜單設定
    global menuObject
    menuObject = object.Menu()

    # 設定菜單設定
    global settingMenuObject
    settingMenuObject = object.SettingMenu()

def menu(event):

    for btn in menuObject.buttons:
        # 事件處理
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menuObject.buttons[btn].click(event):
                if btn == "exit": # 結束遊戲
                    object.GameSetting.running = False
                elif btn == "start":
                    global gameObject
                    gameObject = object.Game()
                    object.GameSetting.gameOver = False
                elif btn == "setting":
                    object.GameSetting.setting = True
        # 物件更新
        menuObject.update(screen)

def settingMenu(event):
    # 事件處理
    if event.type == pygame.MOUSEBUTTONDOWN:
        if settingMenuObject.backButton.click(event):
            object.GameSetting.setting = False
        elif settingMenuObject.lengthBar.upButton.click(event):
            if object.GameSetting.wordLength < 9:
                object.GameSetting.wordLength += 1
        elif settingMenuObject.lengthBar.downButton.click(event):
            if object.GameSetting.wordLength > 1:
                object.GameSetting.wordLength -= 1
        elif settingMenuObject.timesBar.upButton.click(event):
            if object.GameSetting.faildTimes < 9:
                object.GameSetting.faildTimes += 1
        elif settingMenuObject.timesBar.downButton.click(event):
            if object.GameSetting.faildTimes > 1:
                object.GameSetting.faildTimes -= 1
    # 物件更新
    # screen.blit(titleText.textSurface, settingMenuObject.titleText)
    settingMenuObject.update(screen)

def game(event):
    global gameObject
    if event.type == pygame.MOUSEBUTTONDOWN:
        for btn in gameObject.buttons:
        # 事件處理
            if gameObject.buttons[btn].click(event):
                if btn == "back": # 結束遊戲
                    object.GameSetting.gameOver = True
                elif btn == "restart":
                    gameObject = object.Game()
                elif btn == "answer":
                    if gameObject.showAnswer:
                        gameObject.showAnswer = False
                    else:
                        gameObject.showAnswer = True
                    # object.GameSetting.setting = True
    elif event.type == KEYDOWN:
        gameObject.hintEnable = False
        if not gameObject.isComplete:
            if event.key >= ord('a') and event.key <= ord('z'):
                gameObject.addAlpha(chr(event.key))
            elif event.key == K_BACKSPACE:
                gameObject.deleteAplha()
            elif event.key == K_RETURN:
                gameObject.checkWord()
    # 物件更新
    gameObject.update(screen)

def main():
    # 初始設定
    init()

    while object.GameSetting.running: # 程式運行中
        for event in pygame.event.get(): # 讀取事件
            if event.type == pygame.QUIT: # 退出遊戲
                object.GameSetting.running = False
            else:
                screen.fill((0,0,0)) # 背景色
                if object.GameSetting.gameOver: # 遊戲結束
                    if object.GameSetting.setting: # 設定菜單
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
