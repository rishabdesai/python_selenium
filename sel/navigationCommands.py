# ref videos  https://www.youtube.com/watch?v=o3tYiyE_OXE
"""
command to learn
driver.back()
driver.forward()
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.pavantestingtools.com/")
time.sleep(5)
print(driver.title)

driver.get("https://crystalemr.freshdesk.com/support/home")
time.sleep(5)
print(driver. title)

driver.back()
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)

print(driver.title)