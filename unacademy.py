import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # <-- Import the manager

# ... other code ...

chrome_options = Options()
# chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
time.sleep(5)
driver.close()
