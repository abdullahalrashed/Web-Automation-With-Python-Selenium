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
#id and name locators
# driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad Carbon Laptop")

#link text and partial link test

#driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Register").click()

# sliders = driver.find_elements(By.CLASS_NAME, "slider_img")
# print(len(sliders))

# Links = driver.find_elements(By.TAG_NAME, "a")
# print(len(Links)) 72 links




time.sleep(5)
