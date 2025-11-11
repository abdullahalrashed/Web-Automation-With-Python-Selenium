from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
# --- Topic 1: Service Initialization (Automatic Driver Management) ---
print("Initializing Chrome Service and downloading driver...")
chrome_options = Options()
chrome_options.add_argument("--headless=new") 
# --- Topic 2: Driver Initialization ---
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
# Open Facebook login page
driver.get("https://facebook.com/")
driver.maximize_window()

# Wait a bit for the page to load fully
time.sleep(2)

# --- Topic 3: Locators Example ---
# Using CSS Selector for the email input box
# This locator finds the element with id='email'
email_field = driver.find_element(By.CSS_SELECTOR, "input#email")
email_field.send_keys("raashare1@gmail.com")

# Using CSS Selector for the password field
password_field = driver.find_element(By.CSS_SELECTOR, "input#pass")
password_field.send_keys("testpassword")

# Optional: Click the login button
login_button = driver.find_element(By.CSS_SELECTOR, "button[name='login']")
login_button.click()

# Wait before closing (for demo)
time.sleep(5)

driver.quit()
print("Test Completed...")
