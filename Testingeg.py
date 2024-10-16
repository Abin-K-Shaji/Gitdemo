import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



# Initialize the driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/")
driver.implicitly_wait(6)

# Login section
driver.find_element(By.XPATH, "(//a[contains(text(),'Sign In')])[1]").click()
driver.find_element(By.XPATH, "(//input[@id='email'])[1]").send_keys("abinkshaji@gmail.com")
driver.find_element(By.XPATH, "(//input[@id='pass'])[1]").send_keys("password")
driver.find_element(By.XPATH, "(//button[@id='send2'])[1]").click()

# Error handling for login
errromsg = driver.find_element(By.XPATH, "(//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'])[1]").text
print(errromsg)

# assert "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." in errromsg

# Registration section
driver.find_element(By.XPATH, "(//span[contains(text(),'Create an Account')])[1]").click()
# Filling in form details
time.sleep(3)
driver.find_element(By.XPATH, "(//input[@id='firstname'])[1]").send_keys("Abin")
driver.find_element(By.XPATH, "(//input[@id='lastname'])[1]").send_keys("shaji")
driver.find_element(By.XPATH, "(//input[@id='email_address'])[1]").send_keys("Abin05@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Abin@3535")
driver.find_element(By.XPATH, "(//input[@id='password-confirmation'])[1]").send_keys("Abin@3535")
driver.find_element(By.XPATH, "(//button[@title='Create an Account'])[1]").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element(By.XPATH, "(//span[contains(text(),'Edit Address')])[1]").click()
driver.find_element(By.XPATH, "(//input[@id='telephone'])[1]").send_keys("9870564780")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='street_1']").send_keys("seaport road ,kumumpuram")
driver.find_element(By.XPATH, "(//input[@id='city'])[1]").send_keys("kochi")
dropdown= Select(driver.find_element(By.XPATH,"(//input[@id='zip'])[1]"))
dropdown.select_by_visible_text("India")
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@id='city'])[1]").send_keys("670571")
dropdown= Select(driver.find_element(By.XPATH,"(//select[@id='region_id'])[1]"))
dropdown.select_by_visible_text("Kerala")
time.sleep(3)
driver.find_element(By.XPATH, "button[title='Save Address'] span").click()
driver.find_element(By.XPATH, "//a[@aria-label='store logo']//img").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='search']").send_keys("bags")
driver.find_element(By.XPATH, "(//span[normalize-space()='bags for laptop'])[1]").click()






