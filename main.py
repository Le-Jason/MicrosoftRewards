from start import *
from bot import *
import pyautogui

pyautogui.PAUSE = 0.01

def main():
    driver = StartUp()
    clicker = Bot()
    driver.Open()
    driver.Load()
    #Finds signin page and loads it
    signinPic = os.path.join("assets","signin.png")
    clicker.imageFind(signinPic,False,False)
    driver.Load()
    #Enter email
    email = pyautogui.password("Enter Email:")
    pyautogui.write(email)
    pyautogui.press("enter")
    #Enter password
    password = pyautogui.password("Enter Password:")
    passwordPic = os.path.join("assets","password.png")
    clicker.imageFind(passwordPic,False,False)
    pyautogui.write(password)
    pyautogui.press("enter")
    #Press No
    noPic = os.path.join("assets","no.png")
    clicker.imageFind(noPic,False,False)
    #Press Never
    neverPic = os.path.join("assets","never.png")
    clicker.imageFind(neverPic,False,False)
    #Press Signinfree
    signinfreePic = os.path.join("assets","signupfree.png")
    clicker.imageFind(signinfreePic,False,False)
    clicker.Load()

    while(True):
        pass
    driver.Close()

if __name__ == '__main__':
    main()