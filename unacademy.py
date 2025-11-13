import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
# chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)
################ input log in password

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
driver.find_element(By.NAME, "name").send_keys("Abdullah Al Rashed")
driver.find_element(By.NAME, "email").send_keys("RAAshare1@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("abcdefgh")
driver.find_element(By.ID, "exampleCheck1").click()

############### static dropdown

dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select[id = 'exampleFormControlSelect1']"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown.deselect_by_value()
driver.find_element(By.CSS_SELECTOR, "input[type = 'submit'").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

############### Dynamic Dropdown
driver.get("https://www.rahulshetty.com/dropdownpractise/")
driver.find_element(By.ID, "autosuggest ").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class =  'ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "india":
        country.click()
        break

#############changing password

driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("raashare17092@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("@Password1234")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("@Password1234")
driver.find_element(By.XPATH, "//button[text()= 'Save New Password']").click()

############# updating dynamic value

driver.get("https://www.rahulshetty.com/dropdownpractise/")
driver.find_element(By.ID, "autosuggest ").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class =  'ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "india":
        country.click()
        break

print(driver.find_elements(By.ID, "autosuggest").__getattribute__("value"))
assert driver.find_elements(By.ID, "autosuggest").__getattribute__("value") == "india"

time.sleep(5)
driver.quit()
