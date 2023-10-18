import time


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
actual_title=driver.title
expected_title="Automation Testing Practice"
if actual_title==expected_title:
    print("Login Test is passed")
else:
    print("Login Test is failed")


#printing current URL of webpage in the console
print(driver.current_url)

#fetching content of the webpage and storing in to text file(using file handling functions)
text=driver.page_source
file=open("page_source.txt","w")
file.write(text)
file.close()


#providing name
driver.find_element(By.XPATH,'//div[@class="form-group"]//input[@id="name"]').send_keys("Deepa")

#providing email
driver.find_element(By.XPATH,'//div[@class="form-group"]//input[@id="email"]').send_keys("halladamaldeepa123@gmail.com")

#providing  phone number
driver.find_element(By.XPATH,'//div[@class="form-group"]//input[@id="phone"]').send_keys("9945894243")

#Providing address
driver.find_element(By.XPATH,'//div[@class="form-group"]//textarea[@id="textarea"]').send_keys("ABC colony,Belgaum,Karnataka")

#clicking on female button
driver.find_element(By.XPATH,'//input[@id="female"]/parent::div').click()

#selecting all days
elements=driver.find_elements(By.XPATH,'//input[@type="checkbox" and contains(@id,"day")]')
print(len(elements)," are the total number of days")
for day in elements:
  day.click()

'''selecting only one day 
    weekday=day.get_attribute("id")
        if weekday=="sunday":
           day.click()'''

#selecting country name
country_dropdown=Select(driver.find_element(By.XPATH,'//div[@class="form-group"]//select[@id="country"]'))
country_dropdown.select_by_visible_text("India")

#selecting your fevorite colour
driver.find_element(By.XPATH,'//select[@id="colors"]//option[@value="green"]').click()

#selecting Date in calender
DATE="1"
MONTH="November"
YEAR="2021"

driver.find_element(By.XPATH,'//input[@id="datepicker" and @class="hasDatepicker"]').click()
while True:

    mon=driver.find_element(By.XPATH,'//span[@class="ui-datepicker-month"]').text
    year=driver.find_element(By.XPATH,'//span[@class="ui-datepicker-year"]').text
    if MONTH==mon and YEAR==year:
        break

    else:
        driver.find_element(By.XPATH, '//span[text()="Prev" and @class="ui-icon ui-icon-circle-triangle-w"]').click()

dATE=driver.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]/tbody/tr/td/a')
for ele in dATE:
    if ele.text==DATE:
        ele.click()
        break


#opening new link and coming back to the previous page(using naviting commands)
driver.find_element(By.XPATH,'//a[@href="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"]').click()
driver.back()

#printing web table content in console
rows=len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]/tbody/tr'))
cols=len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]/tbody/tr/th'))
print("no. of rows in table are: ",rows)
print("no. of cols in table are: ",cols)

for r in range(2,rows+1):
    for c in range(1,cols+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]")
        print(data.text,end='        ')
    print()



Product=driver.find_element(By.XPATH,'//table[@id="productTable"]//tr[3]/td[4]/input')
Product.click()

#giving data to wikipedia button
driver.find_element(By.XPATH,'//input[@id="Wikipedia1_wikipedia-search-input"]').send_keys("Github")
driver.find_element(By.XPATH,'//input[@class="wikipedia-search-button" and @type="submit"]').click()


#giving data to alertwindow and accepting it
driver.find_element(By.XPATH,'//button[@onclick="myFunctionPrompt()"]').click()
alertwindow=driver.switch_to.alert
alertwindow.send_keys("Deepa")
alertwindow.accept()

#scrolling down the page
driver.execute_script("window.scrollBy(0,500)","")
value=driver.execute_script("return window.pageYOffset;")
print("number of pixels movesd",value)

#doubleclick action
time.sleep(8)
button=driver.find_element(By.XPATH,'//button[@ondblclick="myFunction1()"]')
act=ActionChains(driver)
act.double_click(button).perform()

time.sleep(8)
#drag and drop action
source=driver.find_element(By.XPATH,'//div[@id="draggable"]')
destination=driver.find_element(By.XPATH,'//div[@id="droppable"]')
act.drag_and_drop(source,destination).perform()


driver.execute_script("window.scrollBy(0,500)","")
value=driver.execute_script("return window.pageYOffset;")
print("number of pixels movesd",value)

#sliders
time.sleep(15)
my_slider=driver.find_element(By.XPATH,'//span[@class="ui-slider-handle ui-corner-all ui-state-default"]')
print(my_slider.location)    #{'x': 898, 'y': 1266}
act.drag_and_drop_by_offset(my_slider,100,0).perform()

#switching to frames
time.sleep(15)
frame=driver.find_element(By.XPATH,'//iframe[@id="frame-one796456169"]')
driver.switch_to.frame(frame)
driver.find_element(By.XPATH,'//input[@id="RESULT_TextField-0"]').send_keys("Deepa")
time.sleep(15)
#driver.find_element(By.XPATH,'//input[@id="RESULT_RadioButton-1_1"]').click()

driver.execute_script("window.scrollBy(0,500)","")
value=driver.execute_script("return window.pageYOffset;")
print("number of pixels movesd",value)

#Giving DOB using Datepicker
yr="1992"
mn="January"
dt="20"
driver.find_element(By.XPATH,'//span[@class="icon_calendar"]').click()
y1=Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-year"]'))
y1.select_by_visible_text(yr)
while True:
    m1=driver.find_element(By.XPATH,'//span[@class="ui-datepicker-month"]').text
    if m1==mn:
        break
    else:
        driver.find_element(By.XPATH, '//span[@class="ui-icon ui-icon-circle-triangle-w"]/parent::a').click()

D1=driver.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]//tr/td/a')
for j in D1:
    if j.text==dt:
        j.click()
        break


job=Select(driver.find_element(By.XPATH,'//select[@id="RESULT_RadioButton-3"]'))
job.select_by_visible_text("Automation Engineer")

driver.find_element(By.XPATH,'//input[@id="FSsubmit"]').click()

