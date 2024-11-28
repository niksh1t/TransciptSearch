from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.keys import Keys
#waiting 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options


service= Service(executable_path="chromedriver.exe")
chrome_options = Options()
#chrome_options.add_argument("--headless= new")  # Run in headless mode

#youtube_link= input("enter url: ")
driver = webdriver.Chrome(service= service, options= chrome_options)

youtube_link= input("enter: ") 
driver.get(youtube_link)
more= "//*[@id=\"expand\"]" 
transcript_id= "//*[@id=\"primary-button\"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div"

driver.implicitly_wait(15)

vid_title= "//*[@id=\"title\"]/h1/yt-formatted-string"
title_element= driver.find_element(By.XPATH, vid_title) 
print(title_element.text) 



#wait condition 
'''
WebDriverWait(driver, 20).until(
	EC.presence_of_element_located( (By.LINK_TEXT, more ) )# as a tuple 
)

input_element= driver.find_element(By.XPATH, more)

input_element.click()
input_element= driver.find_element(By.XPATH, transcript_id)
input_element.click()


subtitle_element= driver.find_element(By.ID, "segments-container") 
print(subtitle_element.text)
file = open('sub.txt', 'w')
file.write(subtitle_element.text)

# Access requests via the `requests` attribute

time.sleep(5)
for request in driver.requests:
 if request.method== "POST":
  print(request) 
'''



time.sleep(10)
driver.quit()


