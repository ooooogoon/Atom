from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium import Actionchains
from time import time

time=(2)
driver = webdriver.Chrome("C:/Users/ooooo/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.6/chromedriver.exe")
url = "https://google.com"
driver.get(url)


driver.maximize_window() #창 최대화

action = Actionchains(driver)

driver.find_element_by_css_selector('#gb_70').click()
