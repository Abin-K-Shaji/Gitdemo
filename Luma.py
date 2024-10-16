from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/")
wait = WebDriverWait(driver, 10)  # Explicit wait for up to 10 seconds

# Login section
wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'Sign In')])[1]"))).click()
wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='email'])[1]"))).send_keys("abinkshaji@gmail.com")
wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='pass'])[1]"))).send_keys("password")
wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='send2'])[1]"))).click()

# Error handling for login
errromsg = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'])[1]"))).text
print(errromsg)

# assert "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." in errromsg

# Registration section
wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Create an Account')])[1]"))).click()

# Filling in form details
wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='firstname'])[1]"))).send_keys("Abin")
wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='lastname'])[1]"))).send_keys("shaji")
wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='email_address'])[1]"))).send_keys("Abin95@gmail.com")
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys("Abin@3535")
wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='password-confirmation'])[1]"))).send_keys("Abin@3535")
wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@title='Create an Account'])[1]"))).click()

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Wait for the "Edit Address" button to be clickable and click
wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Edit Address')])[1]"))).click()

# Filling in the address form
wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='telephone'])[1]"))).send_keys("9870564780")
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='street_1']"))).send_keys("seaport road ,kumumpuram")
wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='city'])[1]"))).send_keys("kochi")
dropdown= Select(driver.find_element(By.XPATH,"(//select[@id='country'])[1]"))
dropdown.select_by_visible_text("India")

# Handle dropdowns for country and region
# ZIP code is an input field, so use send_keys instead of Select
wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='zip'])[1]"))).send_keys("670571")

# Now, handle the country and region using Select for dropdowns
region_dropdown = Select(wait.until(EC.presence_of_element_located((By.XPATH, "(//select[@id='region_id'])[1]"))))
region_dropdown.select_by_visible_text("Kerala")

# Save address
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Save Address'] span"))).click()

# Navigate to home by clicking the logo
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='store logo']//img"))).click()

# Search for bags
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))
search_box.send_keys("bags")

# Select the autocomplete suggestion
wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='bags for laptop'])[1]"))).click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Wayfarer Messenger Bag'])[1]"))).click()


hellooo

