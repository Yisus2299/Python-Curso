import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("http://ozh.github.io/cookieclicker/")
wait = WebDriverWait(driver, 20)

# Idioma (cambia a "langSelect-ES" si quieres español)
wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN"))).click()

# Juego listo
wait.until(lambda d: d.execute_script("return Game && Game.ready"))

big_cookie = driver.find_element(By.ID, "bigCookie")

start = time.time()
while time.time() - start < 60:
    big_cookie.click()

diag = driver.execute_script("""
  return {
    cookieClicks: Game.cookieClicks,
    handmadeCookies: Game.handmadeCookies
  };
""")
print(diag)

driver.quit()