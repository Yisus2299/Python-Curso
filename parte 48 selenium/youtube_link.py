from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option(
    "detach", True
)  # el proceso del navegador no se cierra al terminar el script

driver = webdriver.Edge(options=edge_options)
wait = WebDriverWait(driver, 20)

try:
    driver.get(
        "https://www.youtube.com/watch?v=JnUFg6XKHbo&list=RDJnUFg6XKHbo&start_radio=1"
    )

    title_el = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ytd-watch-metadata h1"))
    )
    channel_el = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ytd-channel-name a"))
    )

    print(f"Título: {title_el.text}")
    print(f"Canal: {channel_el.text}")
finally:
    driver.quit()