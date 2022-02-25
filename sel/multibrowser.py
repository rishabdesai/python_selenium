# ref videos  https://www.youtube.com/watch?v=o3tYiyE_OXE
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
# returns title of the page
print(driver.title)
# returns current URL of the page
print(driver.current_url)

# driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
driver.find_element(by=By.XPATH, value=('//*[@id="Tabbed"]/a/button')).click()
time.sleep(5)
# close the browser - which is currently focused
# driver.close()

#to close all the browsers
driver.quit()