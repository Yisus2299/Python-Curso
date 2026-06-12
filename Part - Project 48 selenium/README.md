# Selenium Web Automation Project

## Project Overview
A collection of Selenium WebDriver scripts demonstrating web automation, browser testing, and interactive web application control. This project includes practical examples like cookie clicker automation, Amazon product scraping, and web interaction challenges.

## Technologies Used
- Python 3.x
- Selenium WebDriver
- Microsoft Edge WebDriver (or Chrome/Firefox)
- WebDriverWait (explicit waits)
- Expected Conditions
- Time module for delays

## Project Structure
```
Part - Project 48 selenium/
├── cookieProjectSelenium.py    # Cookie Clicker automation
├── amzon_product.py           # Amazon product scraping
├── ChallengueSelenium.py      # Selenium challenges practice
├── README.md                  # This file
└── chromedriver.exe           # WebDriver binary (if included)
```

## Features
- Browser automation with Edge/Chrome
- Explicit wait conditions for dynamic content
- Element interaction (click, type, submit)
- JavaScript execution in browser context
- Screenshot capture capabilities
- Form automation and data extraction

## Prerequisites

### 1. **Python Installation**
```
python --version  # Should show Python 3.x
```

### 2. **Selenium Installation**
```
pip install selenium
```

### 3. **WebDriver Setup**

#### **Option A: Microsoft Edge**
1. Download Edge WebDriver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
2. Match WebDriver version with your Edge browser version
3. Place `msedgedriver.exe` in project folder or system PATH

#### **Option B: Google Chrome**
1. Download ChromeDriver: https://chromedriver.chromium.org/
2. Match ChromeDriver version with your Chrome browser version
3. Place `chromedriver.exe` in project folder or system PATH

## File Descriptions

### `cookieProjectSelenium.py`
Cookie Clicker game automation:
- Browser initialization and navigation
- Language selection (English/Spanish)
- Element interaction (clicking)
- JavaScript execution for game metrics
- Timed automation (60-second session)

### `amzon_product.py`
Amazon product scraping example:
- Product search automation
- Price extraction and comparison
- Product detail navigation
- Screenshot capture
- Data extraction techniques

### `ChallengueSelenium.py`
Selenium challenges and practice:
- Form automation
- Dropdown selection
- Alert handling
- Window/tab management
- File upload automation

## Code Examples

### Basic Selenium Setup
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Edge browser
driver = webdriver.Edge()
driver.get("http://example.com")

# Wait for element to be clickable
wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.ID, "element-id")))

# Interact with element
element.click()

# Close browser
driver.quit()
```

### Cookie Clicker Automation
```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start browser and navigate to Cookie Clicker
driver = webdriver.Edge()
driver.get("http://ozh.github.io/cookieclicker/")
wait = WebDriverWait(driver, 20)

# Select language (English)
wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN"))).click()

# Wait for game to load
wait.until(lambda d: d.execute_script("return Game && Game.ready"))

# Find the big cookie element
big_cookie = driver.find_element(By.ID, "bigCookie")

# Click for 60 seconds
start = time.time()
while time.time() - start < 60:
    big_cookie.click()

# Get game metrics via JavaScript
metrics = driver.execute_script("""
  return {
    cookieClicks: Game.cookieClicks,
    handmadeCookies: Game.handmadeCookies
  };
""")

print(f"Cookie clicks: {metrics['cookieClicks']}")
print(f"Handmade cookies: {metrics['handmadeCookies']}")

driver.quit()
```

## Common Selenium Operations

### 1. **Element Locators**
```python
# By ID
element = driver.find_element(By.ID, "element-id")

# By Class Name
element = driver.find_element(By.CLASS_NAME, "class-name")

# By CSS Selector
element = driver.find_element(By.CSS_SELECTOR, "div.class-name")

# By XPath
element = driver.find_element(By.XPATH, "//div[@id='element-id']")

# By Link Text
element = driver.find_element(By.LINK_TEXT, "Click Here")

# By Partial Link Text
element = driver.find_element(By.PARTIAL_LINK_TEXT, "Click")
```

### 2. **Wait Strategies**
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Explicit Wait (recommended)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "element-id")))

# Common Expected Conditions
EC.element_to_be_clickable((By.ID, "button-id"))
EC.visibility_of_element_located((By.CLASS_NAME, "visible-class"))
EC.text_to_be_present_in_element((By.ID, "text-element"), "expected text")
EC.title_contains("page title")
```

### 3. **Element Interactions**
```python
# Click element
element.click()

# Type text
element.send_keys("text to type")

# Clear input
element.clear()

# Submit form
element.submit()

# Get element properties
text = element.text
attribute = element.get_attribute("href")
css_value = element.value_of_css_property("color")
```

### 4. **Browser Control**
```python
# Navigation
driver.get("https://example.com")
driver.back()
driver.forward()
driver.refresh()

# Window Management
driver.maximize_window()
driver.set_window_size(1920, 1080)
driver.get_window_position()
driver.get_window_size()

# Screenshots
driver.save_screenshot("screenshot.png")
element.screenshot("element_screenshot.png")

# JavaScript Execution
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
result = driver.execute_script("return document.title;")
```

## Best Practices

### 1. **Use Explicit Waits**
```python
# ❌ Bad - Hardcoded sleep
time.sleep(5)

# ✅ Good - Explicit wait
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "button")))
```

### 2. **Resource Management**
```python
# Always use try/finally or context manager
try:
    driver = webdriver.Edge()
    # Your code here
finally:
    driver.quit()

# Or use context manager (if supported)
with webdriver.Edge() as driver:
    # Your code here
```

### 3. **Error Handling**
```python
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementNotInteractableException
)

try:
    element = driver.find_element(By.ID, "non-existent")
except NoSuchElementException:
    print("Element not found")
except TimeoutException:
    print("Timeout waiting for element")
except ElementNotInteractableException:
    print("Element exists but not interactable")
```

## Common Challenges & Solutions

### 1. **Dynamic Content**
```python
# Wait for AJAX content to load
wait.until(EC.presence_of_element_located((By.ID, "dynamic-content")))
```

### 2. **IFrame Handling**
```python
# Switch to iframe
driver.switch_to.frame("iframe-name")

# Do operations inside iframe
# ...

# Switch back to main content
driver.switch_to.default_content()
```

### 3. **New Tab/Window**
```python
# Get current window handle
main_window = driver.current_window_handle

# Click link that opens new tab
link.click()

# Switch to new tab
for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

# Do operations in new tab
# ...

# Close tab and switch back to main
driver.close()
driver.switch_to.window(main_window)
```

### 4. **File Upload**
```python
# Find file input element
file_input = driver.find_element(By.ID, "file-upload")

# Send file path (not click())
file_input.send_keys("C:/path/to/file.pdf")
```

## Project Purpose
This project demonstrates:
- Web browser automation with Selenium
- Practical automation scenarios (games, e-commerce)
- Best practices for reliable automation
- Error handling and robustness
- Dynamic content interaction
- Cross-browser testing foundations