import selenium
from selenium import webdriver

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select






def intranet(subject,action):
	with open("loginInfo.txt",'r') as f1:
		userId=str(f1.readline().strip('\n'))
		userPass=str(f1.readline())
					
	# Code written by SANDEEP RAJAKRISHNAN , email: sandur43@gmail.com
	# You can send your feedbacks to the above email!!!


	#PREREQUISITES for running the python script (not the .exe file)
	#Python must be installed to run the script 
	#you need to download the chromedriver version corresponding to your chrome version
	#use 'pip install selenium' or 'pip3 install selenium' in your terminal before starting to code.
	#if you dont have pip, install pip first, watch some tutorials on youtube
	#if you encounter errors such as python not internal or external command or that pip is not installed even after installing everything
	#There are videos in youtube that contain the solution

	PATH="chromedriver.exe" #specifying path where chromedriver is stored
	driver=webdriver.Chrome(PATH) #telling the webdriver you have to use "Chrome"driver and passing the path 
	driver.get("https://amritavidya.amrita.edu:8444/cas/login?service=https%3A%2F%2Famritavidya.amrita.edu%3A8444%2Faums%2FJsp%2FCore_Common%2Findex.jsp")
	#navigating to the website url
	

	time.sleep(0)

	try:
		username=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.XPATH,'//*[@id="username"]')))
		#instructing the driver to wait for a maximum of 300seconds for locating the input field on the webpage

		username.send_keys(userId)
		#sending data to the input field


	except:driver.refresh()
	#page reloads if elements don't load after 300 seconds or 5 minutes

	try:
		password=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]')))
		password.send_keys(userPass)
	except:driver.refresh()

	#now we go on and click the submt button (locating it with its XPATH)
	try:
		submit=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.XPATH,'//*[@id="login_form"]/tbody/tr[3]/td[3]/input[3]')))
		submit.click()
	except:
		driver.refresh()

	#when the data is in frames , we cant directly access them , we need to navigate the driver to the frames
	#while dealing with frames in webpages we need to follow the heirarchy of the frames 
	#when we switch between frames , we need to directly come back to the default content (the page that loads at the beginning after login) 
	#and then follow the hierarchy to the next frame

	frame=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.ID,'maincontentframe')))
	#locating the main frame on the webpage which contains other frames (depends on page architecture)	
	frame = driver.find_element_by_id('maincontentframe') 
	#storing the main frame in a variable
	driver.switch_to.frame(frame)
	#switching the driver to main frame

	frame1= driver.find_element_by_name("Iframe")
	driver.switch_to.frame(frame1)
	#this frame is child frame of main frame and the data is inside this
	if(subject<14):
		select_subject = Select(driver.find_element_by_name("htmlPageTopContainer_selCLass")) 
		time.sleep(1)
		select_subject.select_by_index(subject)
		#time.sleep(1)
		subjectSelected = driver.find_element_by_name("htmlPageTopContainer_class3")
		time.sleep(1)
		subjectSelected.click()
		time.sleep(1)

	elif(subject==14):
		subjectSelected = driver.find_element_by_name("htmlPageTopContainer_class2")
		time.sleep(1)
		subjectSelected.click()
		time.sleep(1)

	elif(subject==15):
		subjectSelected = driver.find_element_by_name("htmlPageTopContainer_class1")
		time.sleep(1)
		subjectSelected.click()
		time.sleep(1)

	#for handling dropdowns we need to import Select and then pass the id or name or xpath as shown in the above code
	#then we select the dropdown index

	#then in this case we are selecting the subject that appears at the left side of dropdown after selecting the subject in intranet
	#we give it some time to load, so we use time.sleep, not mandatory but can cause errors , or use implcitly wait to wait for it until it loads ,that would be the best choice



	#now the online exams is in another frame , so we go back to default content(after login) (this won't change data in other frames)
	#and then we go to our desired frame by following the frames heirarchy

	driver.switch_to.default_content()
	#switching to default
	driver.switch_to.frame(frame)
	#going to main frame
	frame1=driver.find_element_by_name("Iframe1")
	driver.switch_to.frame(frame1)
	#switching to the frame which contains online exams 

	list_of_actions=["Assignments","Online Exams","Gradebook","Resources"]

	online_exams=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT,list_of_actions[action])))
	online_exams=driver.find_element_by_link_text(list_of_actions[action])
	online_exams.click()
	#above code navigates to online exams.

	#Thank you, hope you understood the code, this can be customized to be used on other websites or web applications
	#WARNING
	#Some websites can detect selenium or web scrapping , so hitting their API continuosly can lead to an IP block
	#So use it wisely.






