from selenium import webdriver
#from selenium.webdriver.common.keys import keys
driver=webdriver.Chrome()
driver.get("https://www.google.com")
elem=driver.find_element_by_name("q")
elem.send_keys("Hello Sellenium")
elem.submit()
driver.close
