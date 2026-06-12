# Import Selenium and locators for class, id, and other selectors
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Use Edge as the testing browser and keep it open after the script finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# Create and configure the Edge webdriver
driver = webdriver.Edge(options=edge_options)

# Navigate to the desired page
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Focus on an anchor tag using a CSS selector
# CSS selectors are useful when elements have no class or ID and you need to locate specific structure
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a") # "#" means ID; HTML uses div id="articlecount"
# article_count.click() # this would click the located element

# Find element by link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals") # locate a link on the page
# all_portals.click()

# Find the "Search" input by NAME:
# 1) Click the search icon to open the text field
wait = WebDriverWait(driver, 10)
search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.search-toggle")))
search_button.click()

# 2) Type into the visible search field
search_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.cdx-text-input__input[name='search']")))
# search_box.send_keys("Python") # this types the query into the search field

# send the query and press Enter
search_box.send_keys("Python", Keys.ENTER) # this enters the query and submits it with Enter

