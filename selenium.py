from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os 
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)
driver.maximize_window()

driver.get("https://www.ilovepdf.com/pdf_to_word")
time.sleep(5)
s = driver.find_element(By.ID,'pickfiles').send_keys("file.pdf")
#file path specified with send_keys
time.sleep(200)
