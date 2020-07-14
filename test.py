import selenium
from selenium import webdriver

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
def configure():
	f1=open('SUBJECT LIST.txt','a')
	f1.seek(0);f1.truncate();
	f2=open('configuration.txt','w')
	f2.write("false")
	f3=open('loginInfo.txt','r')
	userId=str(f3.readline().strip('\n'))
	userPass=str(f3.readline())

	PATH="chromedriver" #specifying path where chromedriver is stored
	driver=webdriver.Chrome(PATH) #telling the webdriver you have to use "Chrome"driver and passing the path 
	driver.get("https://amritavidya.amrita.edu:8444/cas/login?service=https%3A%2F%2Famritavidya.amrita.edu%3A8444%2Faums%2FJsp%2FCore_Common%2Findex.jsp")

	try:
		username=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.XPATH,'//*[@id="username"]')))
			#instructing the driver to wait for a maximum of 300seconds for locating the input field on the webpage

		username.send_keys(userId)
			#sending data to the input field


	except:
		driver.refresh()
		#page reloads if elements don't load after 300 seconds or 5 minutes

	try:
		password=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]')))
		password.send_keys(userPass)
	except:
		driver.refresh()

	try:
		submit=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.XPATH,'//*[@id="login_form"]/tbody/tr[3]/td[3]/input[3]')))
		submit.click()
	except:
		driver.refresh()




	def collectClassInfo(frame):
		driver.switch_to.default_content()
			#switching to default
		driver.switch_to.frame(frame)
			#going to main frame
		frame1=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.NAME,"Iframe1")))
		driver.switch_to.frame(frame1)

		classInfo=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT,"Class Info")))
		classInfos=driver.find_element_by_link_text("Class Info")
		classInfo.click()

		infoFrame=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.TAG_NAME,"iframe")))

		driver.switch_to.frame(infoFrame)
		content=driver.find_element_by_xpath('/html/body/div/div').text
		
		print(content.split("_")[1])
		f1.write(content.split("_")[1]+"\n")
		driver.switch_to.default_content()

		

	i=0
	try:
		while True:	
			frame=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.ID,'maincontentframe')))
				#locating the main frame on the webpage which contains other frames (depends on page architecture)	
			frame = driver.find_element_by_id('maincontentframe') 
				#storing the main frame in a variable
			driver.switch_to.frame(frame)
				#switching the driver to main frame

			frame1= WebDriverWait(driver,300).until(EC.presence_of_element_located((By.NAME,"Iframe")))

			driver.switch_to.frame(frame1)

			select_subject = Select(driver.find_element_by_name("htmlPageTopContainer_selCLass")) 
			time.sleep(1)
			select_subject.select_by_index(i)
			#time.sleep(1)
			subjectSelected = WebDriverWait(driver,300).until(EC.presence_of_element_located((By.NAME,'htmlPageTopContainer_class3')))
			time.sleep(1)
			subjectSelected.click()
			time.sleep(1)
			driver.switch_to.default_content()
			#switching to default
			driver.switch_to.frame(frame)
				#going to main frame
			frame1=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.NAME,"Iframe1")))
			driver.switch_to.frame(frame1)

			classInfo=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT,"Class Info")))
			classInfos=driver.find_element_by_link_text("Class Info")
			classInfo.click()

			infoFrame=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.TAG_NAME,"iframe")))

			driver.switch_to.frame(infoFrame)
			content=driver.find_element_by_xpath('/html/body/div/div').text
			
			print(content.split("_")[1])
			f1.write(content.split("_")[1]+"\n")
			driver.switch_to.default_content()
			i=i+1
	except:
			print("no more subjects in dropdown")
			

	driver.switch_to.default_content()



	
	frame=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'maincontentframe')))
	#locating the main frame on the webpage which contains other frames (depends on page architecture)	
	frame = driver.find_element_by_id('maincontentframe') 
	#storing the main frame in a variable
	driver.switch_to.frame(frame)
	#switching the driver to main frame

	frame1= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"Iframe")))
	driver.switch_to.frame(frame1)

	#time.sleep(1)
	subjectSelected = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"htmlPageTopContainer_class1")))
	time.sleep(1)
	subjectSelected.click()
	driver.switch_to.default_content()
	#switching to default
	driver.switch_to.frame(frame)
		#going to main frame
	frame1=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.NAME,"Iframe1")))
	driver.switch_to.frame(frame1)

	classInfo=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT,"Class Info")))
	classInfos=driver.find_element_by_link_text("Class Info")
	classInfo.click()

	infoFrame=WebDriverWait(driver,300).until(EC.presence_of_element_located((By.TAG_NAME,"iframe")))

	driver.switch_to.frame(infoFrame)
	content=driver.find_element_by_xpath('/html/body/div/div').text
	
	print(content.split("_")[1])
	f1.write(content.split("_")[1]+"\n")
	driver.switch_to.default_content()


	f1.close()
	f2.seek(0)
	f2.truncate()
	f2.write("true")
	f2.close()
	f3.close()
	driver.quit()
	return True
c=configure()