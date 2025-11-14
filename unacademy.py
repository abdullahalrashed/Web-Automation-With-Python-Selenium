import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
# chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)
driver.implicitly_wait(2)

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

############### Check box Dynamically

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox'] ")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

############### hideable and non dynamic check box

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox'] ")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, 'hide-textbox').click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

############### java alert popping up

Myname = "Rashed"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(Myname)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

alert_key = driver.switch_to.alert
alert_key_text = alert_key.text
print(alert_key_text)
assert Myname in alert_key_text
alert_key.accept()  # to click the OK button to accept the alert pop up
# alert_key.dismiss()  # to reject the alert , presumably the 'cancel' button

################ explicit and implicit waiting via selenium
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[class = 'search-keyword']").send_keys("ber")
time.sleep(1)
results = driver.find_elements(By.XPATH, "//div[@class = 'products']/div")
count = len(results)
print(len(results))
assert count > 0
#### parent to child XPATH
for result in results:
    result.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, "img[alt = 'Cart'").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.XPATH, "//span[text() = 'Code applied ..!']").text)
driver.find_element(By.XPATH, "//button[text() = 'Place Order']").click()
time.sleep(4)
driver.quit()
