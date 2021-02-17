from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#Launch browser
driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\Functions\selenium\chromedriver.exe")
#load url
driver.get("http://adactinhotelapp.com/")
t=driver.get("http://adactinhotelapp.com/")
print(type(t),t)
c=driver.current_url
print(c,type(c))
x=driver.name
print(x)


#find the element in locators of username textbox by inspect and validate it accordingly
username=driver.find_element(By.XPATH,"//input[@type='text']")
# send_keys is a method of webelement class
username.send_keys("nitishselvakumar")
#get_attribute is amethod to get the user input has given it stores in value attribute
r=username.get_attribute("value")
print(r,type(r))
# find the element of passordtextbox by inspect and validate it accordingly
password=driver.find_element(By.XPATH,"//input[@type='password']")
## send_keys is a method of webelement class
password.send_keys("s1740034")
k=password.get_attribute("value")
print(k,type(k))
btn_login=driver.find_element(By.XPATH,"//input[@type='Submit']")
btn_login.click()


table=driver.find_elements(By.CLASS_NAME,"content")
print(table)
t_rows=driver.find_elements(By.TAG_NAME,"tr")
for each_row in t_rows:
    t_data=each_row.find_elements(By.TAG_NAME,"td")
    for each_data in t_data:
        d = each_data.text
        if d=="Welcome to Adactin Group of Hotels":
            print(d)
        x= each_data.text

        if x=="Search Hotel":
            print(x)








# z=txt_adatainwebpage.text
# print(type(z),z)
# txt_searcpagetext=driver.find_element((By.XPATH,"//td[text()',Search Hotel ']"))
# x=txt_searcpagetext.text
# print(type(x),x)

