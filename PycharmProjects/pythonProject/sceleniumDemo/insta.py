
# import selenium
import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(1)
# username=driver.find_element("name","username")
username=driver.find_element("xpath",'//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys('sruthi')
time.sleep(1)
pwd=driver.find_element("name","password")
pwd.send_keys('123')
time.sleep(3)
pwd.submit()

time.sleep(5)


# //*[@id="loginForm"]/div/div[3]/button

# //*[@id="loginForm"]/div/div[3]/button/div
# //*[@id="loginForm"]/div/div[3]/button
# //*[@id="loginForm"]/div/div[3]