from browser import *
from bot import *
import pyautogui
import os 

pyautogui.PAUSE = 0.01


def main():
    driver = Browser()
    clicker = Bot()
    driver.Open()
    driver.Load()

    #Finds signin page and loads it
    signinPic = os.path.join("assets","signin.png")
    clicker.imageFind(signinPic,False,False)
    driver.Load()

    #Enter email
    email = ""
    pyautogui.write(email)
    pyautogui.press("enter")

    #Enter password
    # password = pyautogui.password("Enter Password:")
    passwordPic = os.path.join("assets","password.png")
    clicker.imageFind(passwordPic,False,False)
    password =""
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
    # xbutton = os.path.join("assets","xbutton.png")
    # clicker.imageFind(xbutton,False,False)

    undonePic = os.path.join("assets","undone.png")
    clicker.imageFind(undonePic,False,False)
    signin2 = os.path.join("assets","signin2.png")
    clicker.imageFind(signin2,False,False)
    driver.tab()
    correctPic = os.path.join("assets","nextquestion.png")
    driver.Load()
    driver.textQuiz()
    clicker.imageFind(correctPic,False,False)
    driver.textQuiz()
    clicker.imageFind(correctPic,False,False)
    driver.textQuiz()

    while(True):
        pass
    driver.Close()

if __name__ == '__main__':
    main()