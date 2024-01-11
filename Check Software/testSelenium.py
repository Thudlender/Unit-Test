from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import time

class ResearchTest(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver
        s = Service('D:\webdriver\chromedriver-win64')
        self.driver = webdriver.Chrome(service=s)
           
    def tearDown(self):
        # Close the browser
        self.driver.quit()
    
    def test_search_bykeyword(self):
         

        # Open Google
        self.driver.get("http://www.google.com")

        # Find the search box element and enter a query
        search_box =  self.driver.find_element(By.NAME,"q")
        search_box.send_keys("NPRU")

        # Perform the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the search results to load
        time.sleep(5)

        # Print the title of the current page
        print( self.driver.title)

        # Close the browser
        self.driver.quit()

        page_content = self.driver.page_source
        self.assertIn("มหาวิทยาลัยราชภัฏนครปฐม", page_content, "Not in Page")

if __name__ == "__main__":
     unittest.main()