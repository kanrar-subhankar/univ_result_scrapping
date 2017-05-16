from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
from bs4 import BeautifulSoup as soup 
import csv
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()
roll=16900114001
while(roll<169001141120):
	
	driver=webdriver.Firefox()
	driver.implicitly_wait(60)
	driver.get("http://www.makautexam.net/GradeCardGenerateAndPrint.aspx?qs=6w3FCS3zLOk%3d")
	elem=driver.find_element_by_name("txtrollcode")
	elem.clear()
	elem.send_keys(roll)
	try:
		select_value=driver.find_element_by_css_selector("select#ddlSemister > option[value='05']").click()
	except NoSuchElementException:
		print "WTF"
		pass
	driver.find_element_by_xpath("//input[@name='btnContinue']").click()
	try:
		alert = driver.switch_to_alert()
		alert.accept()
	except NoAlertPresentException:
		print "Bal"
		pass
	
	try:
		wait=WebDriverWait(driver,10)
		wait.until(EC.presence_of_element_located((By.ID,'DetailsPanel')))
		page_html_name_user=driver.find_element_by_id('lblroll')
		page_soup=soup(page_html_name_user.text,"html.parser")
		page_html_sem_marks_user=driver.find_element_by_id('lblsgpaodd')
		page_soup2=soup(page_html_sem_marks_user.text,"html.parser")
		print page_soup,
		print page_soup2
		with open("content.txt","a") as f:
			r=csv.writer(f)
			r.writerow([page_soup,page_soup2])
		f.close()
		driver.quit()
	except TimeoutException:
		print "CHECK YOUR FUCKING INTERNET CONNECTION"
		exit()	
	
	roll+=1
	