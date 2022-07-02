import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from start import *
import os

pyautogui.PAUSE = 0.01

class Bot:
    def __init__(self):
        self.browser = 1
    
    def search(self):
        self.tab()

    def imageFind(self,image,g,double):
    #Finds the image and clicks on it(This was made by https://www.youtube.com/watch?v=GYw_voBfawA NOT ME)
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
        
    def check(self):
    #Helper function that locates a pixel location
        time.sleep(2)
        print(pyautogui.position())