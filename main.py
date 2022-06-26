from start import *
import pyautogui

pyautogui.PAUSE = 0.01

def main():
    driver = StartUp()
    driver.Open()
    driver.Close()

if __name__ == '__main__':
    main()