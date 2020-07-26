from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/ooooo/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.6/chromedriver.exe")
url = "https://google.com"
driver.get(url)

driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('파이썬')
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)

driver.find_element_by_css_selector('.LC20lb.DKV0Md').click()
# driver.find_elements_by_css_selector('.LC20lb.DKV0Md')[1].click() #element's' 가 되어야지 검색결과 2번째 클릭 가능
