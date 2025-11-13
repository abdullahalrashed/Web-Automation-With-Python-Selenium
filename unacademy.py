import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # <-- Import the manager

# ... other code ...

chrome_options = Options()
# chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)

driver.find_element(By.NAME, "name").send_keys("Abdullah Al Rashed")
driver.find_element(By.NAME, "email").send_keys("RAAshare1@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("abcdefgh")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[type = 'submit'").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
time.sleep(5)
driver.close()
