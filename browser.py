from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Browser:
    #Class starts up the program and leads towards the home page of the rewards page
    def __init__(self):
        self.PATH = "C:\Program Files (x86)\chromedriver.exe" #Location of the chrome driver
        self.delay = 3 # seconds #Delay for loading pages
        self.tabCounter = 0
        self.quizCounter  = 0

    def Open(self):
    #Main method to open and load rewards page
        #Turns off "Automation extension item pop up"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        #Opens Chrome
        self.browser = webdriver.Chrome(executable_path=self.PATH,chrome_options=options)
        self.browser.maximize_window()
        self.browser.get("https://www.microsoft.com/en-us/rewards")
        
    def Close(self):
    #Closes the browser
        self.browser.quit()

    def Load(self):
    #Make sures that the page is loaded
        try:
            myElem = WebDriverWait(self.browser, self.delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
        except TimeoutException:
            pass
    
    def tab(self):
        if self.tabCounter == 0:
            self.tabCounter = 1
            self.browser.switch_to.window(self.browser.window_handles[self.tabCounter])
        else:
            self.tabCounter = 0
            self.browser.switch_to.window(self.browser.window_handles[self.tabCounter])
    
    def tabClose(self):
        self.browser.close()
        self.tabCounter = 0

    def correctQuiz(self):
        self.quizCorrect = self.browser.find_element("class name","wk_hideCompulsary")
        self.quizCorrect.find_element("xpath","..").click()
        
    
    def textQuiz(self):
        action = ActionChains(self.browser)
        self.quizCorrect = self.browser.find_element(By.CLASS_NAME,"wk_hideCompulsary")
        q = self.quizCorrect.find_element(By.XPATH,"..")
        # self.browser.execute_script("arguments[0].scrollIntoView();", q)
        # self.browser.execute_script("arguments[0].click();", q)
        action.click(on_element = q).perform()
        