import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class WebAutomaton(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox(executable_path='/home/orine/Desktop/geckodriver')
    def searchSquares(self, search_site, search_element):
        driver = self.driver
        driver.get(search_site)
        elem = driver.find_element_by_name(search_element)
        elem.send_keys("Square")
        elem.send_keys(Keys.RETURN)
    def closeDown(self):
        self.driver.close()

if __name__ == "__main__":
    automaton = WebAutomaton()
    automaton.setUp()
    automaton.searchSquares(search_site="https://www.youtube.com/", search_element= "search_query")