#conditional command statements in selenium automation for webpage application
#is_dispalyed,is_enabled the space of login button of username and password
# is_selected is for to know the radio button selected or not

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
driver.get("http://www.facebook.com")
print(driver.title)
user_element=driver.find_element(By.XPATH,"//input[@name='email']")
user_element.send_keys("mohammadferoz_21@yahoo.co.in")
print(user_element.get_attribute('value'))
print("staust of the username column:",user_element.is_displayed())
print("staus of the usernsme:",user_element.is_enabled())
user_password=driver.find_element(By.XPATH,"//input[@name='pass']")
user_password.send_keys("shareef@yasin")
print(user_password.get_attribute('value'))
print("status of userpassword:",user_password.is_displayed())
print("staus of the userpassword:",user_password.is_enabled())
driver.save_screenshot("conitional command of selenium on web page.png")
time.sleep(5)
driver.quit()


