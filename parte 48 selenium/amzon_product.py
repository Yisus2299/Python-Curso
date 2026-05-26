from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://www.amazon.com/-/es/dp/B08H5WSGD9/ref=dp_cr_wdg_tit_rfb")

price = driver.find_element(By.CLASS_NAME, value = "a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, value = "a-price-fraction")
product_name = driver.find_element(By.ID, value = "productTitle")
platform = driver.find_element(By.CLASS_NAME, value="a-text-bold")
print(f"Price: {price.text}.{price_fraction.text}$")
print(f"Product Name: {product_name.text}")
print(f"Platform: {platform.text}")
driver.quit()