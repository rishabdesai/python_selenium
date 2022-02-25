# ref videos  https://www.youtube.com/watch?v=o3tYiyE_OXE
"""
command to learn:
is_dispayed()
is_enabled()
is_selected()
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://crystalemr.freshdesk.com/support/home")
# ele = driver.find_element_by_name("term")
ele= driver.find_element(by=By.NAME, value="term")
time.sleep(5)
print(ele.is_displayed())  # return True/False based on element status
print(ele.is_enabled())



