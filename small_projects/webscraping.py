from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path='/home/orine/Desktop/geckodriver')

driver.get("https://copyassignment.com/")

search_element = driver.find_element_by_id("is-search-input-0")

text = "Turtle"
search_element.send_keys(text)
