import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os

pyautogui.PAUSE = 0.01

class StartUp:
    def __init__(self):
        self.PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.delay = 3 # seconds
        
    def check(self):
        time.sleep(2)
        print(pyautogui.position())

    def Open(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])

        self.browser = webdriver.Chrome(executable_path=self.PATH, chrome_options=options)
        self.browser.maximize_window()
        self.browser.get("https://www.microsoft.com/en-us/rewards")
        self.Load()

        signinPic = os.path.join("assets","signin.png")
        self.imageFind(signinPic,False,False)
        self.Load()

        pyautogui.write("######@gmail.com")
        pyautogui.press("enter")
        password = pyautogui.password("Enter Password:")
        passwordPic = os.path.join("assets","password.png")
        self.imageFind(passwordPic,False,False)
        pyautogui.write(password)
        pyautogui.press("enter")
        noPic = os.path.join("assets","no.png")
        self.imageFind(noPic,False,False)

        time.sleep(10)
    
    def Close(self):
        self.browser.quit()

    def Load(self):
        try:
            myElem = WebDriverWait(self.browser, self.delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
        except TimeoutException:
            pass
    
    def imageFind(self,image,g,double):
        #https://www.youtube.com/watch?v=GYw_voBfawA
        a = 0
        b = 0
        while(a==0 and b==0):
            try:
                im = pyautogui.locateCenterOnScreen(image,confidence=0.65,grayscale=g)
                a = im[0]
                b = im[1]
            except TypeError:
                pass
        if double == True:
            pyautogui.doubleClick(a,b)
        else:
            pyautogui.click(a,b)