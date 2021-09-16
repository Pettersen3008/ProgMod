from selenium import webdriver

PATH = '~/Downloads/geckodriver'

driver = webdriver.Firefox(PATH)
driver.get('https://google.com')

driver.close()