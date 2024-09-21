
''' this is the first program in selenium'''
import time
from selenium import webdriver

driver = webdriver.Chrome() # define the browser
driver.get("https://www.facebook.com/")# link of the page facebook

# Creating a Reference of Form For Finding Email and Password
driver.find_element("id","email").send_keys("vinu")
driver.find_element("id","pass").send_keys("123456")
driver.find_element("name","login").click()

time.sleep(5)
#x-path->  //*[@id="u_0_9_mG"]