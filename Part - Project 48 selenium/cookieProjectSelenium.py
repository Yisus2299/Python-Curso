import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# start an Edge browser and navigate to Cookie Clicker
driver = webdriver.Edge()
driver.get("http://ozh.github.io/cookieclicker/")
wait = WebDriverWait(driver, 20)

# Language selector (use "langSelect-ES" for Spanish)
wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN"))).click()

# wait until the game is ready
wait.until(lambda d: d.execute_script("return Game && Game.ready"))

big_cookie = driver.find_element(By.ID, "bigCookie")

# click the big cookie for 60 seconds
start = time.time()
while time.time() - start < 60:
    big_cookie.click()

# fetch some metrics from the game
diag = driver.execute_script("""
  return {
    cookieClicks: Game.cookieClicks,
    handmadeCookies: Game.handmadeCookies
  };
""")
print(diag)

driver.quit()