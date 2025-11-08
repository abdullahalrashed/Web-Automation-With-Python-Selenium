from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


# --- Topic 1: Service Initialization (Automatic Driver Management) ---
# This line automatically downloads the correct ChromeDriver version
# that matches your installed Google Chrome browser.
print("Initializing Chrome Service and downloading driver...")
service = Service(ChromeDriverManager().install())

# --- Topic 2: Driver Initialization ---
# The driver is created using the automatically managed service object.
driver = webdriver.Chrome(service=service)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad Carbon Laptop")

time.sleep(5)
