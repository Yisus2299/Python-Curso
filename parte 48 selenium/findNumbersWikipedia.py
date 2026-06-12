from selenium import webdriver
from selenium.webdriver.common.by import By

#keep chrome/edge browser open after program fiishes

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

#create and configure the edge/Chrome wbdriver

driver = webdriver.Edge(options=edge_options)

#Navigate to wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Focus on an anchor tag using CSS selectors (use this when elements have no classes or IDs and you need to inspect a div)
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a") # "#" means ID; the HTML uses div id="articlecount"
english_article = driver.find_element(By.CSS_SELECTOR, value="#articlecount li:nth-child(2) a")
print(article_count.text)
print(english_article.text)

driver.quit()