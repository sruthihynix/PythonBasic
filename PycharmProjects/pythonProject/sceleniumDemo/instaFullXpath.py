''' instagram login automation using selenium'''

import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(2)
user=driver.find_element("xpath","/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
user.send_keys('sruthi65190')
time.sleep(2)
pwd=driver.find_element("xpath","/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
# pwd=driver.find_element('xpath',"//*[@id=""]/div/div[2]/div/label/input")
pwd.send_keys('9048')
time.sleep(2)
# driver.find_element("xpath","/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div").click()
pwd.submit()
time.sleep(5)
# //*[@id="loginForm"]/div/div[1]/div/label/input
# //*[@id="loginForm"]/div/div[1]/div/label/span