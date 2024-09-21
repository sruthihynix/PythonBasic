
# import selenium
import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.instagram.com/')

user=driver.find_element("name","username").send_keys('sruthi65190')
pwd=driver.find_element("name","password").send_keys('9048133580')
driver.find_element("xpath","/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button").submit()

time.sleep(10)


# login=driver.find_element("xpath","//input[@type ='submit']")
# //*[@id="loginForm"]/div/div[1]/div/label/input
#full xpath -- /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button
#xpath //*[@id="loginForm"]/div/div[3]/button