# The challenge is to fill a signup form on Lab Report using Selenium (see iteraction.py)
# import Selenium helpers and locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Use Edge as the test browser
# keep browser open after the script finishes for debugging
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# create and configure the Edge webdriver
driver = webdriver.Edge(options=edge_options)

# navigate to the target page
driver.get("https://secure-retreat-92358.herokuapp.com/")

# organize the script: 1) find page elements
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
sign_up = driver.find_element(By.CSS_SELECTOR, value="form button")

# 2) fill the fields
first_name.send_keys("Jesus")
last_name.send_keys("Ziegler")
email.send_keys("testJesusZ@email.com")

# click the sign-up button to submit the form
sign_up.click()