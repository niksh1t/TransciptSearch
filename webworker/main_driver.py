from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time 


#waiting 
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC 


video_title= "" 

def video_title():
	global video_title 
	return video_title 


def get_sub(yt_url):
	service= Service(executable_path="chromedriver.exe")
	chrome_options = Options()
	#chrome_options.add_argument("--headless= new")  # Run in headless mode
	
	driver = webdriver.Chrome(service= service, options= chrome_options)
	driver.implicitly_wait(20)
	
	driver.get(yt_url)
	
	more_element= "//*[@id=\"expand\"]" 
	transcript_element_id= "//*[@id=\"primary-button\"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div"
	
	vid_title= "//*[@id=\"title\"]/h1/yt-formatted-string"
	title_element= driver.find_element(By.XPATH, vid_title) 
	global video_title
	video_title= title_element.text 

	input_element= driver.find_element(By.XPATH, more_element)
	input_element.click()

	input_element= driver.find_element(By.XPATH, transcript_element_id)
	input_element.click()

	subtitle_element= driver.find_element(By.ID, "segments-container") 

	
	#create dictionary of sub 
	'''
	raw_sub= subtitle_element.text

	raw_sub_lines= raw_sub.splitlines()
	sub_dict= {}

	for i in range(0, len(raw_sub_lines), 2):
		key= raw_sub_lines[i]
		value= raw_sub_lines[i+1] 
		sub_dict[key]= value

	
	#print(sub_dict)
	
	with open("output.txt", "w", encoding="utf-8") as file:
		for value in sub_dict.values(): 
			file.write(value + "\n")
	'''

	time.sleep(10)
	driver.quit()
	#return sub_dict


