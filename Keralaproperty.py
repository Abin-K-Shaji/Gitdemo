import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Initialize the driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://keralaproperty.in/")
driver.implicitly_wait(6)

# Login section
driver.find_element(By.CSS_SELECTOR, ".login").click()
driver.find_element(By.ID, "ulogin").send_keys("Abinkshaji")
driver.find_element(By.ID, "upass").send_keys("password")
driver.find_element(By.ID, "sub_logbtn").click()

# Error handling for login
errromsg = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/form/span/center").text
assert "Invalid Login Credentials." in errromsg

# Registration section
driver.find_element(By.XPATH, "//a[contains(text(),'New user')]").click()

# Selecting from dropdown
dropdown = Select(driver.find_element(By.ID, 'listowner'))  # Corrected dropdown element
dropdown.select_by_visible_text("Property Owner")

# Filling in form details
time.sleep(3)
driver.find_element(By.XPATH, "(//input[@id='utitle'])[1]").send_keys("Abin")
driver.find_element(By.ID, "umail").send_keys("Abin35@gmail.com")
driver.find_element(By.ID, "memberpass").send_keys("Abin35")
time.sleep(3)
driver.find_element(By.ID, "repass").send_keys("Abin35")  # Ensure passwords match
driver.find_element(By.ID, "umobile").send_keys("9089786756")

# Submitting the form
driver.find_element(By.ID, "sub_regbutton").click()

# Handling alert
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.accept()

driver.find_element(By.XPATH, "(//input[@id='ulogin'])[1]").send_keys("abin") 

