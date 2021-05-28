from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome('/Users/shubh/Desktop/d/chromedriver') 
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
  
# Replace 'Friend's Name' with the name of your friend  
# or the name of a group  
target = '"Shivam Upadhyay"'
  
# Replace the below string with your own message 
string = "Hi"
  
x_arg = '//span[contains(@title,' + target + ')]'
target= wait.until(EC.presence_of_element_located(( By.XPATH, x_arg))) 
target.click() 

input_box=driver.find_element_by_class_name('DuUXI')
for i in range(100): 
    input_box.send_keys(string + Keys.ENTER) 
    time.sleep(1) 