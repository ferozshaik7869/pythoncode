# from selenium import webdriver
#
# # to launch chrome browser
# driver = webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# # to load url
# driver.get("https://www.facebook.com/")
# # to get the tittle of the webpage
# t = driver.title
# print(t)
# print(type(t))
# # to get the url of the page
# url = driver.current_url
# print(url)
# print(type(url))

# *********************************************
# to launch Firefox browser
#
# driver=webdriver.Firefox(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\geckodriver.exe")
# #to launch url
# driver.get("https://login.yahoo.com/manage_account?lang=en-US&done=https%3A%2F%2Fmail.yahoo.com%2F&src=ym&signin=true&eid=100")
# # to gettittle of the webpage
# t=driver.title
# print(t)
# print(type(t))
# #to get url page
# url=driver.current_url
# print(url)
# print(type(url))
# **************************************************
# to launch the IE driver
# driver=webdriver.Ie(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\IEDriverServer.exe")
# # to load url
# driver.get("https://www.udemy.com/")
# t=driver.title
# print(t)
# print(type(t))
# #to get url of the page
# url=driver.current_url
# print(url)
# print(type(url))
# **********************************************
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://www.selenium.dev/documentation/en/webdriver/")
# t=driver.title
# print(t,type(t))
# url=driver.current_url
# print(url,type(url))
# *********************************************
# driver=webdriver.Firefox(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\geckodriver.exe")
# driver.get("https://www.google.com/search?q=python+%2Bselenium+jobs+in+hyderabad&rlz=1C1RLNS_enIN868IN868&oq=pyth&aqs=chrome.1.69i57j69i59l3j35i39j69i60l3.4501j0j7&sourceid=chrom")
# t=driver.title
# print(t,type(t))
# url=driver.current_url
# print(url,type(url))
# ********************************************
# from selenium import webdriver
# driver=webdriver.Ie(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\IEDriverServer.exe")
# driver.get("https://www.google.com/search?q=tcs+careers&rlz=1C1RLNS_enIN868IN868&oq=tcs&aqs=chrome.3.69i57j46i67i199i291i433j0i67j0i67i433j0i433j0i67l3.5213j0j7&sourceid=chrome&ie=UTF-8")
# t=driver.title
# print(t,type(t))
# url=driver.current_url
# print(url,type(url))
# x=driver.name
# print(x,type(x))
# ****************************************************
# locators:id,name,classname,xpath,tagname,linktest,css selector
# webelement:c
# send_keys()-m--->to send/pass keys
# To maximize the window we have Method
# driver.maximize_window(there is no return type for this)
# DOM -Structure is Document object module
# in the Element inspect we got the below format
# <input type="text" class="inputtext _55r1 _6luy"
# name="email" id="email" data-testid="royal_email"
# placeholder="Email address or phone number" autofocus="1"
# aria-label="Email address or phone number">
# in which we have the elements as follows
# Ever filed we have purple color --->tagname
# brown color---->attribute names
# blue color--->attribute values
# and in the above file in html format with open <html.header>
# and <\html><body> close tag
# ****************************************
# from selenium import webdriver
# #to launch the chrome browser
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# #to load the url
# x=driver.get("http://www.facebook.com")
# print(x,type(x))
# #to maximize the window
# driver.maximize_window()
# # to find the element for username
#  to launch the login button
# driver.fullscreen_window()
# # to get the title of the webpage of browser
# t=driver.title
# print(t,type(t))
# # to get the url of the web page of browser
# url=driver.current_url
# print(url,type(url))
# #to quit browser
# driver.quit()
# txt_username=driver.find_element_by_id("email")
# txt_username.send_keys("mohammedferoz_210@yahoo.com")
# print(txt_username,type(txt_username))
# #to find the element of password
# txt_password=driver.find_element_by_name("pass")
# txt_password.send_keys("shareef@yasin")
# print(txt_password,type(txt_password))
#
# ***********************************
# from selenium import webdriver
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# y=driver.get("http://www.facebook.com")
# print(y,type(y))
# t=driver.title
# print(t,type(t))
# url=driver.current_url
# print(url,type(url))
# txt_username=driver.find_element_by_id("email")
# print(txt_username,type(txt_username))
# txt_username.send_keys("mohammadferoz_210@yahoo.co.in")
# txt_password=driver.find_element_by_name("name")
# print(txt_password,type(txt_password))
# txt_password.send_keys("shareef@yasin")
# driver.maximize_window()
# driver.fullscreen_window()
# driver.quit()
# **********************************
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://www.facebook.com")
# print(driver.get("http://www.facebook.com"))
# driver.maximize_window()
# driver.fullscreen_window()
# txt_username=driver.find_element_by_id("email")
# txt_username.send_keys("mohammadferoz_210@yahoo.co.in")
# txt_password=driver.find_element(by=By.NAME, value="name")
# txt_password.send_keys("shareef@yaseen")
# butn_login=driver.find_element(By.XPATH,"(//(button[@name='login'])")
# butn_login.click()
# driver.quit()
# ************************
import keyboard
from selenium import webdriver, common
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# url = driver.get("http://www.facebook.com")
# print(url)
# driver.maximize_window()
# txt_username = driver.find_element(By.ID, "email")
# txt_username.send_keys("mohammad_210@yahoo.co.in")
# txt_password = driver.find_element(By.NAME, "pass")
# txt_password.send_keys("shareef@yasin")
# butn_login = driver.find_element(By.XPATH, "//button[@value='1']")
# butn_login.click()
# time.sleep(5)
# driver.quit()

# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# url=driver.get("http://www.facebook.com")
# driver.maximize_window()
# title=driver.title
# print(title)
# txt_username=driver.find_element(By.XPATH,("//input[@id='email']"))
# txt_username.send_keys("shaikmohammedferoz79@gamil.com")
# txt_password=driver.find_element(By.XPATH,("//input[@placeholder='Password']"))
# txt_password.send_keys("shareef@yaseen")
# btn_login=driver.find_element(By.XPATH,("//button[@name='login']"))
# btn_login.click()
# time.sleep(10)
# driver.quit()

# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://demo.automationtesting.in/Index.html")
# print(driver.title)
# print(driver.current_url)
# txt_username=driver.find_element(By.XPATH,"//body[@ng-app='Registerform']")
# txt_username.send_keys("kursheed7869@gmail.com")
# btn_login=driver.find_element(By.XPATH,"//img[@id='enterimg']")
# btn_login.click()
# txt_firstname=driver.find_element(By.XPATH,"//input[@ng-model='FirstName']")
# txt_firstname.send_keys("kursheed")
# txt_lastname=driver.find_element(By.XPATH,"//input[@ng-model='LastName']")
# txt_lastname.send_keys("shaik")
# txt_adress=driver.find_element(By.XPATH,"//textarea[@ng-model='Adress']")
# txt_adress.send_keys("sivaramnagar 4th lane,26-20-135,chuttugunta,Guntur-522004")
# txt_uploadimage=driver.find_element(By.XPATH,"//input[@id='imagesrc']")
# # txt_uploadimage.click()
# x=driver.page_source
# print(x)
# txt_emailadress=driver.find_elements(By.XPATH,"//input[@ng-model='EmailAdress']")
# txt_emailadress.send_keys("ferozsky99@gamil.com")
# txt_phonenumber=driver.find_element(By.XPATH,"//input[@ng-model='Phone']")
# txt_phonenumber.send_keys("9966864874")
# txt_gender=driver.find_element(By.XPATH,"//input[@ng-model='radiovalue']")
# txt_gender.send_keys("Female")
# time.sleep(10)
# driver.quit()
# *********************************************************
# text:
# //tagname[text()='textvalue'] we need to inspect the text in the webpage and validate text
# we have to go by xpath element
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://www.facebook.com")
# t=driver.title
# print(t)
# driver.maximize_window()
# txt_create=driver.find_element(By.XPATH,"//a[text()='Create a Page']")
# t=txt_create.text
# print(t,type(t))
# txt_fb=driver.find_element(By.XPATH,"//h2[contains(text(),'you')]")
# t1=txt_fb.text
# print(t,type(t))
# ****************************
# to know the attribute value in the web elements i.e when we inspect the element in webpage
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.common.keys import Keys
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://www.facebook.com")
# t=driver.title
# print(t,type(t))
#
# txt_username=driver.find_element(By.ID,"email")
#
# att=txt_username.get_attribute("placeholder")
# at=txt_username.get_attribute(("autofocus"))
# print(att,type(att))
# print(at,type(at))
# *************************
# to get the data intial value by passing send keys like email id and password
# if we want to inspect ,actual what we have typed in,and what is the resultant practically
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://www.facebook.com")
# t=driver.title
# print(t)
# print(driver.title)
# txt_username=driver.find_element(By.ID,"email")
# txt_username.send_keys("mohammaderoz_210@yahoo.co.in")
# att=txt_username.get_attribute('value')
# print(att)
# txt_password=driver.find_element(By.NAME,"pass")
# txt_password.send_keys("shareef@yasin")
# at=txt_password.get_attribute('value')
# print(at)
# bnt_login=driver.find_element(By.XPATH,"//button[@value='1']")
# t1=bnt_login.click()
# print(t1,type(t1))
# time.sleep(5)
# driver.quit()
# **********************************
# Debug :used to excute the code line by line
# step:1)we need to set break pont where you want
# step:2)run the debug (rightclick)
# step over/for execution line by line
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://www.facebook.com")
# t=driver.title
# print(t,type(t))
# # txt_username=driver.find_element(By.ID,"email")
# # txt_username.send_keys("shaikmohammedferoz79@gamil.com")
# # t2=txt_username.get_attribute("value")
# # print(t2)
# txt_username1=driver.find_element(By.XPATH,"//input[@type='text']")
# txt_username1.send_keys("mohammadferoz_210@yahoo.co.in")
# t3=txt_username1.get_attribute('value')
# print(t3)
# # txt_password=driver.find_element(By.NAME,"pass")
# # txt_password.send_keys("shareef@yasin")
# # t4=txt_password.get_attribute('value')
# # print(t4,type(t4))
# txt_password1=driver.find_element(By.XPATH,"//input[@placeholder='Password']")
# txt_password1.send_keys("shareef@yasin")
# t5=txt_password1.get_attribute('value')
# print(t5,type(t5))
# txt_create=driver.find_element(By.XPATH,"//a[text()='Create a Page']")
# t6=txt_create.text
# print(t,type(t6))
# txt_fb=driver.find_element(By.XPATH,"//h2[contains(text(),'helps')]")
# t7=txt_fb.text
# print(t7,type(t7))
#
# driver.quit()
# time.sleep(5)

# **************************
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://www.snapdeal.com/ ")
# t=driver.title
# print(t)
# att=driver.current_url
# print(att)
# txt_search=driver.find_element(By.XPATH,"//input[@id='inputValEnter']")
# txt_search.send_keys("iphone",Keys.ENTER)
#
# txt_link=driver.find_element(By.XPATH,"//a[text()='iphones 7']")
# txt_link.click()
#
# enter_pin=driver.find_element(By.XPATH,"//input[@placeholder='Enter your pincode']")
# enter_pin.send_keys("522004",Keys.ENTER)
#
# check_click=driver.find_element(By.XPATH,"//button[@class='pincode-check']")
# check_click.click()
# print(check_click.is_selected())


# ************************************************************************88


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://www.facebook.com")
# url=driver.current_url
# print(url,type(url))
# txt_username=driver.find_element(By.XPATH,"//input[@name='email']")
# txt_username.send_keys("mohammadferoz_210@yahoo.co.in")
# t10=txt_username.get_attribute('value')
# print(t10)
# txt_password=driver.find_element(By.XPATH,"//input[@aria-Label='Password']")
# txt_password.send_keys("shareef@yasin")
# t9=txt_password.get_attribute('value')
# print(t9)
# txt_create=driver.find_element(By.XPATH,"//a[text()='Create a Page']")
# t11=txt_create.text
# print(t11,type(t11))
# txt_fbtext=driver.find_element(By.XPATH,"//h2[contains(text(),'help')]")
# t12=txt_fbtext.text
# print(t12,type(t12))
# print("before click login button",driver.current_url)
# # btn_create=driver.find_element(By.XPATH,"//a[@role='button']")
# # btn_create.click()
# btn_login=driver.find_element(By.XPATH,"//button[@type='submit']")
# btn_login.click()
# print("After click login button",driver.current_url)
#
# t13=driver.save_screenshot("createlogin.png")
# print(t13,type(t13))
#
# time.sleep(5)
# driver.quit()
# *********************************************************
# to navigate from one webpage to another page

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://www.facebook.com")
# print(driver.title)
# url=driver.current_url
# print(url)
# time.sleep(2)
# driver.get("https://www.google.com")
# print(driver.title)
# url1=driver.current_url
# print(url1)
# time.sleep(2)
# driver.back()
# print(driver.title)
# url=driver.current_url
# print(url)
# time.sleep(2)
# driver.forward()
# print(driver.title)
# url1=driver.current_url
# print(url1)
# time.sleep(5)
# driver.quit()
# *****************************************
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http:www.yahoomail.com")
# print(driver.title)
# url=driver.current_url
# print(url)
# time.sleep(2)
# driver.get("http:www.google.com")
# print(driver.title)
# url=driver.current_url
# print(url)
# driver.back()
# time.sleep(2)
# print(driver.title)
# url=driver.current_url
# print(url)
# driver.forward()
# print(driver.title)
# url=driver.current_url
# print(url)
# time.sleep(2)
# driver.quit()
# ***************************************************************

# Action Chains:
# move_to_element()-->method
# drag_and_drop()--->method
# perform()--->method
# To do mouse over action :
# move_to_element()-->m

#  synatx:
#  objectName=Actionchains(webdriver ref)
# objectName.move_to_element(webElement ref).perform()

# to drag and drop:
# drag_and_drop()--->m

# objectName=Actionchains(webdriver ref)
# objectName.drag_and_drop(source,destination).perform()

#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# # to load the url
# driver.get("https://www.greenstechnologys.com/")
# # to capture the tittle of url
# s=driver.title
# print(s)
# driver.maximize_window()
# opt_course=driver.find_element(By.XPATH,"//a[text()='COURSES']")
# #object creation
# acc=ActionChains(driver)
# #to perform mouse over action
# acc.move_to_element(opt_course).perform()
# opt_remote=driver.find_element(By.XPATH,"//span[text()='Robotic Process Automation Training']")
# acc.move_to_element(opt_remote).perform()
# btn_remote=driver.find_element(By.XPATH,"//span[text()='Robotic Process Automation Training']")
# btn_remote.click()
# view_schudule=driver.find_element(By.ID,"popupModal")
# acc.move_to_element(view_schudule).perform()
# driver.quit()
# **********************************************
# same as above mouse over actions using Actionchains Class
# importing the related packages as follows
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# # to launch the webbrowser
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# #to launch the url
# driver.get("https://nareshit.in/")
# t=driver.title
# s=driver.current_url
# #to capture the url,title
# print("title of the url",type(t),t)
# print("url",type(s),s)
# #get the webElement from the url to go through actions as follows:
# software_training=driver.find_element(By.XPATH,"//body[@itemtype='https://schema.org/WebPage']")
# #object created for ActionChains
# acc=ActionChains(driver)
# # to perform mouse over Action As follows
# acc.move_to_element(software_training).perform()
# #get the webElement by XPath from webpage
# course_schu=driver.find_element(By.XPATH,"//body[@itemtype='https://schema.org/WebPage'][1]")
# acc.move_to_element(course_schu).perform()
# ******************************************************
# same as mouse overaction on webpage Amazon
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import select
# import time
#
# # to launch the web browswer
# driver = webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# # to load the url
# driver.get("https://www.amazon.com/")
# # to capture the tittle
# d = driver.title
# print(type(d))
# print(d)
# # to capture the current url
# c = driver.current_url
# print(c)
# print(type(c))
# # to get the webElement from url fro action over mouse
# acc_signin = driver.find_element(By.XPATH, "//span[text()='Account & Lists']")
# # to create an object for ActionChains
# acc = ActionChains(driver)
# # to perform Action as follows
# acc.move_to_element(acc_signin).perform()
# print(acc)
# print(type(acc))
# order_item = driver.find_element(By.XPATH, "//a[@id='nav_prefetch_yourorders']")
# acc.move_to_element(order_item).perform()
# time.sleep(2)
# x = driver.back()
# print(x)

# ***********************************************************

# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver import remote
# from selenium.webdriver.common.service import Service
#
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://www.greenstechnologys.com/")
# print(driver.title)
# driver.maximize_window()
# opt_cou=driver.find_element(By.XPATH,"//a[text()='COURSES']")
# # to create an object
# s=ActionChains(driver)
# # to perform mouse over action
# s.move_to_element(opt_cou).perform()
#
# opt_oracle=driver.find_element(By.XPATH,"//span[text()='Oracle Training']")
# s.move_to_element(opt_oracle).perform()
#
# btn_sql=driver.find_element(By.XPATH,"//span[text()='SQL Certification']")
# btn_sql.click()
# driver.quit()
# ********************************************************************8888
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# driver = webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://demo.guru99.com/test/drag_drop.html")
# driver.maximize_window()
# src = driver.find_element(By.XPATH, "//li[@id='credit1']")
# dcs = driver.find_element(By.XPATH, "////ol[@id='loan']")
# # print(dcs)
# # print(src)
# acc = ActionChains(driver)
# acc.drag_and_drop(src,dcs)
# # driver.quit()
# ********************************************************
# keyboard Actions
# Right click:
# objectName=Actionchains(webdriver ref)
# objectName.context_click(webElement ref).perform()
#
# double click:
# objectName=Actionchains(webdriver ref)
# objectName.double_click(webElement ref).perform()
#
# keyboard Actions:
# keyboard:Method
# press()-function
# release()-function
# *************************************************
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome(executable_path=r'C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe')
# driver.get("http://www.google.com")
# driver.maximize_window()
# btnGmail=driver.find_element(By.XPATH,"//a[text()='Gmail']")
# acc=ActionChains(driver)
# # to perform right click
# acc.context_click(btnGmail).perform()
# time.sleep(2)
# driver.implicitly_wait(10)
#
# btnImages=driver.find_element(By.XPATH,"//a[text()='Images']")
# acc.context_click(btnImages).perform()
# time.sleep(2)
# driver.quit()
# ******************************************************
# double click
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# import keyboard
# import time
#
# driver = webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://www.google.com")
# driver.maximize_window()
# btnGmail = driver.find_element(By.XPATH, "//a[text()='Gmail']")
# acc = ActionChains(driver)
# acc.context_click(btnGmail).perform()
#
# for i in range(3):
#     keyboard.press("down")
#     keyboard.release("down")
#     time.sleep(1)
#
# keyboard.press("enter")
# keyboard.release("enter")
# driver.quit()

# **********************************************
# # # double click:
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# import keyboard
# import time
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://www.facebook.com/")
# time.sleep(2)
# txt_username=driver.find_element(By.ID,"email")
# txt_username.send_keys("mohammadferoz_210@yahoo.co.in")
#  ********************************************************************
# Alert :class
# switching the alert :as we cannot able to inspect the element we go for actions on alert
# refName=driver.switch_to.alert
# types:
# simple Alert--->contains only ok button(we should accept the alert)
# confirm alert---->contains both ok and cancel button(Either we can accept or dismiss this alert)/
# prompt alert--->contains text box with ok and cancel button,we have to insert 'yes' to accept the alert
# Methods in Alert:
# accept()-->method to accept the alert
# dismiss()--->method to dismiss the alert
# send_keys()--->method to insert the values
# text()--->method to print the text from the Alert
# ********************************************************************************
# simple Alert how to handle
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# # to load the url
# driver.get(" http://demo.automationtesting.in/Alerts.html")
# driver.maximize_window()
# btn_Alert = driver.find_element(By.XPATH, "//button[@onclick='alertbox()']")
# btn_Alert.click()
# #After clcik abve  we haveto handle the alert as follows:
# #switch to alert
#
# al = driver.switch_to.al
# print(type(al),al)
# time.sleep(2)
# #to handle alert
# al.accept()
#
# driver.quit()
#we can aslo handle the simple alert awith keyboard button Excape:
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #to launch the browser
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# # to load the url
# driver.get("http://demo.automationtesting.in/Alerts.html")
# 
# btn_Alert = driver.find_element(By.XPATH, "//button[@onclick='alertbox()']")
# btn_Alert.click()
# # handle the alert first switch to alert
# al = driver.switch_to.alert
# # al.accept()
# time.sleep(2)
# 
# keyboard.press("ESC")
# keyboard.release('ESC')
# driver.quit()
# *************************************
# confirm alert to handle
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # to launch the browser
# driver = webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\ferozproject\Chrome\chromedriver.exe")
# # to load the url
# driver.get("http://demo.automationtesting.in/Alerts.html")
# link_alert = driver.find_element(By.XPATH, "//a[text()='Alert with OK & Cancel ']")
# link_alert.click()
# btn_alert = driver.find_element(By.XPATH, "//button[@onclick='confirmbox()']")
# btn_alert.click()
#
# time.sleep(2)
# # to handle the alert in confirm alert
# al = driver.switch_to.alert
#
# # al.dismiss()# to click cancel button
# # print(type(al),al)
#
# driver.quit()

# prompt box alert handle
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\ferozproject\Chrome\chromedriver.exe")
# driver.get("http://demo.automationtesting.in/Alerts.html")
#
# link_alert = driver.find_element(By.XPATH, "//a[text()='Alert with Textbox ']")
# link_alert.click()
# btn_alert = driver.find_element(By.XPATH, "//button[@onclick='promptbox()']")
# btn_alert.click()
# # time.sleep(2)
# # handle the prompt alert of text box
# al = driver.switch_to.alert
# print(al.text)
# al.send_keys("yes")
# # al.send_keys("No")
# # print(al.text)
# # al.dismiss()# if you want to click cancel button
# # to get the text from the alert
# driver.quit()


# ****************************************************************************
# java script Executoar
# uses of javascript Executor
# 1)if send keys and click method not working we go for the javascript Executor
# 2)scroll down and scroll up operation can be performed
# 3)easy to interact with hiddenelement and fastest one
# 4)High light webElement

# webDriver:class
# execute_script("javascriptcode",webElement ref)-method
#
# insert---method
# arguments[0].setAttribute('value','Greens')
#
# click:
# arguments[0].click()
#
# get-attribute:
# return arguments[0].getAttribute('value')

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# # to load the url
# driver.get("https://www.facebook.com/")
# # to maximize the window
# driver.maximize_window()
# txt_username=driver.find_element(By.ID,"email")
# #to insert the value by using java script executer code
# driver.execute_script("arguments[0].setAttribute('value','mohammadferoz_210@yahoo.com')",txt_username)
# #to get the attribute values by using javascript code
# s=driver.execute_script("return arguments[0].getAttribute('value')",txt_username)
# print(s,type(s))
# txt_password=driver.find_element(By.NAME,"pass")
# driver.execute_script("arguments[0].setAttribute('value','shareef@yasin')",txt_password)
# r=driver.execute_script("return arguments[0].getAttribute('value')",txt_password)
# print(type(r),r)
# btn_login=driver.find_element(By.XPATH,"//button[@value='1']")
# btn_login.click()
# driver.quit()

# ******************************************************************************************

# java script Executer
# webDriver:C
# execute_script("javascriptcode',webElement ref")---m
# scroll down:
# arguments[0].scrollIntoview(true)-down

# Scroll up:
# argumnets[0],scrollIntoview(false)-up


# to highlighting the webElement
# arguments[0].setAttribute('style','background:yellow;border:2px solid red;');


# scrolldown and scrollup methods as folows
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# # to load url
# driver.get("https://www.facebook.com/")
# # t=driver.title
# # print(t,type(t))
# time.sleep(2)
# driver.maximize_window()
# down=driver.find_element(By.XPATH,"//li[text()='English (UK)']")
# # down=driver.find_element(By.XPATH,"//a[@title='log in to Facebook']")
# driver.execute_script("arguments[0].scrollIntoView(true)",down)
# # driver.execute_script("arguments[0].scrollIntoView(true)",down)
# time.sleep(3)
# up=driver.find_element(By.ID,"email")
# driver.execute_script("arguments[0].scrollIntoView(false)",up)

# *************************************************************************
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# txt_username=driver.find_element(By.ID,"email")
# # driver.execute_script("arguments[0].setAttribute('style','background:blue;border:2px solid green;')",txt_username)
# driver.execute_script("arguments[0].setAttribute('style','background:green;border:3px solid yellow;')",txt_username)
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://www.gmail.com")
# txt_username=driver.find_element(By.XPATH,"//input[@type='email']")
# driver.execute_script("arguments[0].setAttribute('style','background:green;border:4px solid yellow;')",txt_username)

# ****************************************************************
''  # Frames:
# DOM Syntax:
# <iframe id="876" "name="h86g"/>"
# <frameset>
#
# the methods of frames as follows:
# driver.switch_to.frame(id)
# diver.switch_to.frame(name)
# driver.switch_to.frame(webElement ref)
# driver.switch_to.frame(index)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://demo.guru99.com/test/guru99home/")
#
# #to switch the frame by id
# driver.switch_to.frame("a7aa5e07")
# btn_lgn=driver.find_element(By.XPATH,"//img[@src='Jmeter720.png']")
# btn_lgn.click()
# ***************************************************
# The below program as below but here we are initizaling with ID
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # import time
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://demo.guru99.com/test/guru99home/")
# # webElement for frame
# f=driver.find_element(By.ID,"a077aa5e")
# #to swithc to frame by webElement
# driver.switch_to.frame(f)
# btn_img=driver.find_element(By.XPATH,"//img[@src='Jmeter720.png']")
# btn_img.click()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import  Keys
# import time
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://www.amazon.com/")
# txt_search=driver.find_element(By.ID,"twotabsearchtextbox")
# txt_search.send_keys("iphone",Keys.ENTER)
#
#
# lnk_iphone=driver.find_element(By.XPATH,"//span[text()='Tracfone Apple iPhone 7 4G LTE Prepaid Smartphone - 32GB - Black - Carrier Locked']")
# lnk_iphone.click()
#
# btn_addcart=driver.find_element(By.XPATH,"//input[@id='add-to-cart-button']")
# btn_addcart.click()
#
# btn_cart=driver.find_element(By.XPATH,"//a[@id='hlb-view-cart-announce']")
# btn_cart.click()
#
# driver.quit()

# to control the cursor from current window to parent window follow the procedure
# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
#
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://www.amazon.com/")
# t=driver.title
# print(t)
#
# txt_searchbox=driver.find_element(By.ID,"twotabsearchtextbox")
# txt_searchbox.send_keys("samsung",Keys.ENTER)
#
#
# lnk_samsung=driver.find_element(By.XPATH,"//span[text()='Samsung Galaxy S20 FE 5G | Factory Unlocked Android Cell Phone | 128 GB | US Version Smartphone | Pro-Grade Camera, 30X Space Zoom, Night Mode | Cloud Navy']")
# lnk_samsung.click()
#
# # to handle the  currentwindow/parent window
# parent_window_id=driver.current_window_handle
# print(type(parent_window_id),parent_window_id)
#
# # to handle all windows
# all_window_id=driver.window_handles
# print(all_window_id,type(all_window_id))
#
#
# #to switch to current window
# for each_window_id in all_window_id:
#     if each_window_id !=parent_window_id:
#         driver.switch_to.window(each_window_id)
#
# print(each_window_id)
# time.sleep(3)
#
# btn_cart=driver.find_element(By.XPATH,"//input[@id='add-to-cart-button']")
# btn_cart.click()
#
# driver.quit()
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://www.amazon.com/")
# t=driver.title
# print(t)
#
# txt_board=driver.find_element(By.XPATH,"//input[@type='text']")
# txt_board.send_keys("bicycle",Keys.ENTER)
#
# lnk_bicycle=driver.find_element(By.XPATH,"//img[@alt='Sponsored Ad - Schwinn Hopscotch & Toggle Quick Build Kids Bike, 12-16-Inch Wheels, Smart Start Steel Frame, Easy Tool-Fre...']")
# lnk_bicycle.click()
#
#
# par_window_id=driver.current_window_handle
# print(par_window_id)
# print(type(par_window_id))
#
# all_windows_id=driver.window_handles
# print(all_windows_id,type(all_windows_id))
#
# driver.switch_to.window(all_windows_id[0])
#
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://www.amazon.com/")
# s=driver.current_url
# print(s)
# t=driver.title
# print(t)
#
# txt_bar=driver.find_element(By.ID,"twotabsearchtextbox")
# txt_bar.send_keys("skatebooards",Keys.ENTER)
#
#
# type_item=driver.find_element(By.XPATH,"//span[text()='KO-ON Complete Skateboards for Beginners and Kids 31 inches x 7.88 inches, Standard 7-ply Layers Canadian Maple Wood with Double Kicktails and Radial Concave for Tricks'] ")
# type_item.click()
#
# par_window_id=driver.current_window_handle
# print(type(par_window_id),par_window_id)
#
# all_windows_id=driver.window_handles
# print(type(all_windows_id),all_windows_id)
#
# driver.switch_to.window(all_windows_id[0])
#
#
# add_tocart=driver.find_element(By.XPATH,"//span[@text()='Add to Cart']")
# add_tocart.click()

# driver.switch_to.window(all_windows_id[0])
#
# type_item=driver.find_element((By.XPATH,"//img[@src='https://m.media-amazon.com/images/I/81ediHTWayL._AC_UL320_.jpg'] "))
# type_item.click()

# driver.quit()

# ***************************************************************************************
# Drop Down html code
# <select>
# <option value="ind">indai</option>
# <option value="us">united states</option>
# </select>

# select
# select_by_index(10)
# select_by_value("IND")
# select_by_visible_text("India")

# objectNmae=ClassName()
# ref=Select(WebElement refName)

# Select:C
# Select_by_index()---M
# Select_by_value()----M
# Select_by_visible_text()---M
# deSelect_by_index()----M
# deSelect_by_vale()----M
# deSelect_by_visible_text()----M
# deselect_all()----M
# is amultiple---f

# ********************************************************
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# import time
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://facebook.com/")
# t=driver.title
# print(t)
# s=driver.current_url
# print(s)
#
# btn_create_new=driver.find_element(By.XPATH,"//a[text()='Create New Account']")
# btn_create_new.click()
#
# time.sleep(3)
#
# dd_month=driver.find_element(By.ID,"month")
# # to create the object for the select
# s=Select(dd_month)
# # to select the value by indexing
# # s.select_by_index(5)
# # to select the value by using value
# s.select_by_value("10")
# # to check the drop down is single selected and multiple selected
# print(s.is_multiple)
#
# driver.quit()
#
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time


# driver = webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("http://facebook.com/")
# driver.maximize_window()
#
# btn_create_new = driver.find_element(By.XPATH, "//a[text()='Create New Account']")
# btn_create_new.click()
#
# time.sleep(3)
#
# dd_month = driver.find_element(By.XPATH, "//select[@title='Month']")
#
# # to create the object for the select
# s = Select(dd_month)
# s.select_by_value("6")
# op = s.options
# print(op)
# print(type(op))
# for i in op:
#     print(i.text)

# **********************************************
# methods for selecting the scroll options of multiple options:
# select_by_value()
# select_by_index()
# select_by_visibletext()
# methods for deselecting the options
# deselect_by_value()
# deselect_by_index()
# deselect_by_visibletext()
#
# deselect_all()
#
# first_selected_option
# all_selected_options
# ****************************************************************
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# import time
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
# ddcountry=driver.find_element(By.XPATH,"//select[@id='multi-select']")
# s=Select(ddcountry)
# print(s.is_multiple)
# s.select_by_value("New York")
# s.select_by_index(0)
# s.select_by_visible_text("Texas")
# time.sleep(2)
# driver.quit()
# ******************
# to deselect all selected options as follows
# s.deselect_all()
# time.sleep(2)
# ************
# to get the first selected option from the drop down
# op=s.first_selected_option
# print(op.text)
# to print the text of seleceted which option is selected
# op1=s.all_selected_options
# for i in op1:
#     print(i.text)

# To select the option using index:
# op2=s.options
# for index,item in enumerate(op2):
#     s.select_by_index(index)
#     print(index)
# To select the options using value:
# op3=s.options
# for index,value in enumerate(op3):
#     t=value.text
#     s.select_by_visible_text(t)
#     print(t)
# to select the options using the attribute value
# op4=s.options
# for index,value in enumerate(op4):
#     att=value.get_attribute("value")
#     s.select_by_visible_text(att)
#     print(att)
# driver.quit()

# To Select the option using even index:
# op5=s.options
# for index,value in enumerate(op5):
#     if index % 2 ==0:
#         s.select_by_index(index)
#         print(index)

# **********************************************************
# Webtable:
# <table>
# <tr>
# <th>id</th>
# <th>name</th>
# <th>email</th>
# </tr>
#
# <tr>
# <td>123</td>
# <td>sam</td>
# <td>sam@gmail</td>
# </tr
#
# </table>
# tr-table row
# td=table data
# th=table heading
# id:123  name:sam email:sam@gmail.com

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
#
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://www.w3schools.com/html/html_tables.asp")
# driver.get_screenshot_as_png()
# a=driver.title
# print(a)
# url=driver.current_url
# print(url)
# for i in url:
#     print(i)
#
# table=driver.find_element(By.ID,"customers")
# # to fetch rows from table
# t_row=table.find_elements(By.TAG_NAME,"tr")
# #iterate each_row from rows from row table
# for each_row in t_row:
#     t=each_row.text
#     print(t)
# *************************************************************
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://www.w3schools.com/html/html_tables.asp")
# t=driver.title
# print(t)
# url1=driver.current_url
# print(url1)
# table=driver.find_elements(By.ID,"customers")
# print(table)
#
# t_rows=driver.find_elements(By.TAG_NAME,"tr")
# # to fetch rows from table
# for each_row in t_rows:
#     # to fetch
#     t_data=each_row.find_elements(By.TAG_NAME,"td")
#     for each_data in t_data:
#         att=each_data.text
#         print(att)
# ************************************************************************
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://www.w3schools.com/html/html_tables.asp")

# t=driver.title
# print(t)
# att=driver.current_url
# print(att)
#
# table=driver.find_element(By.ID,"customers")
# print(table)
#
# t_row=table.find_elements(By.TAG_NAME,"tr")
# for each_row in t_row:
#      t_header=each_row.find_elements(By.TAG_NAME,"th")
#      for each_header in t_header:
#          x=each_header.text
#          print(x)
#      t_data=each_row.find_elements(By.TAG_NAME,"td")
#      for each_data in t_data:
#          n=each_data.text
#          if n == "UK":
#              print(n)

# # **********************************************************************
# driver.get("https://www.w3schools.com/html/html_tables.asp")
# t = driver.title
# print(t)
# n = driver.current_url
# print(n)
# table=driver.find_element(By.ID, "customers")
# table_row=table.find_elements(By.TAG_NAME,"tr")
# for row_index,each_row in enumerate(table_row):
#     t_data=each_row.find_elements(By.TAG_NAME,"td")
#     for coloumn_index,each_data in enumerate(t_data):
#         data=each_data.text
#         if data== "Mexico":
#             print(data)
# *********************************************************************************
# table=driver.find_element(By.ID,"customers")
# t_row=table.find_elements(By.TAG_NAME,"tr")
# t=t_row[1].text
# print(t)
# x=t_row[2].text
# print(x)
# n=t_row[3].text
# print(n)
# driver.quit()
# *******************************************************************************************
# Automation of jagannna amma vadi webpage
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# import time
# driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
# driver.get("https://ammavodihm1.apcfss.in/AMMAVODI_MIS/serachUidforAmmavadiOutSd11122020421.htm")
# print(driver.title)
# print(driver.current_url)
# stu_dist=driver.find_element(By.XPATH,"//select[@name='dyna(district_code)']")
# print(stu_dist)
# student=Select(stu_dist)
# print(student)
# student.select_by_visible_text("GUNTUR")
# op=student.options
#
# print(op)
# print(type(op))
# for i in op:
#     print(i.text)
# adhaar_dts=driver.find_element(By.XPATH,"//select[@id='type_code']")
# print(adhaar_dts)
# adhaar=Select(adhaar_dts)
# adhaar.select_by_visible_text("--Mother Aadhar--")
# g=(adhaar.select_by_visible_text("--Mother Aadhar--"))
# print(g)
# op1=adhaar.options
# for n in op1:
#     print(n.text)
# adhaar_number=driver.find_element(By.XPATH,"//input[@type='text'][1]")
# v=adhaar_number.send_keys("23070178098")
# print(v)
# verfication_id=driver.find_element(By.XPATH,"//input[@name='dyna(passlineNormal)']")
# verfication_id.send_keys("1234",Keys.ENTER)
#
# get_details=driver.find_element(By.XPATH,"//input[@type='button']")
# get_details.click()
# *******************************************************
# Navigation cammands
# WebElements:Class
# is_displayed()----text box,button are displayed or not.
# is_enabled()----to check buttons and text buttons and textboxes are edited
# is_selected()--- to check buttons are selected or not
# Web Driver:Class
# forward()---move forward
# back()---return back to pervious page
# refresh()-- to refresh webpage

# ********************************
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Ie(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\IEDriverServer.exe")
# driver.get("https://ammavodihm1.apcfss.in/AMMAVODI_MIS/serachUidforAmmavadiOutSd11122020421.htm")
