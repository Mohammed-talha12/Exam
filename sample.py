# 9th c

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class RegistrationFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080")  # Your containerized app URL

    def test_form_submission(self):
        driver = self.driver
        
        # Fill in the form fields
        driver.find_element(By.NAME, "name").send_keys("John Doe")
        driver.find_element(By.NAME, "email").send_keys("john@example.com")
        driver.find_element(By.NAME, "phone").send_keys("9876543210")
        
        # Select event
        event_dropdown = driver.find_element(By.NAME, "event")
        event_dropdown.send_keys("Workshop")
        
        # Add comment
        driver.find_element(By.NAME, "comments").send_keys("Looking forward!")
        
        # Submit form
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        
        time.sleep(2)  # Wait for page response

        # Example verification (check page title or alert)
        self.assertIn("Registration", driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
