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

driver.get("https://facebook.com/")
driver.maximize_window()

# tag and ID,class,attribute

#tag_and_ID= driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("raashare1@gmail.com")
driver.find_element(By.CSS_SELECTOR,'input[class=''').send_keys("raashare1@gmail.com")
#driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("raashare1@gmail.com")













time.sleep(5)