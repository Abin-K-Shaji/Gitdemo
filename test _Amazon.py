import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://keralaproperty.in/")
driver.implicitly_wait(6)

driver.find_element(By.CSS_SELECTOR,".login").click()
driver.find_element(By.ID,"ulogin").send_keys("Abinkshaji")
driver.find_element(By.ID,"upass").send_keys("password")
driver.find_element(By.ID,"sub_logbtn").click()
errromsg =driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div/form/span/center").text
assert "Invalid Login Credentials." in errromsg
driver.find_element(By.XPATH,"//a[contains(text(),'New user')]").click()
dropdown=Select(driver.find_element(By.XPATH,"(//select[@id='listowner'])[1]").click())
dropdown.select_by_visible_text("Property Owner")
time.sleep(3)
driver.find_element(By.ID,"(//input[@id='utitle'])[1]").send_keys("Abin")
time.sleep(3)
driver.find_element(By.ID,"umail").send_keys("Abin35@gmai.com")
driver.find_element(By.ID,"memberpass").send_keys("Abin35")
driver.find_element(By.ID,"repass").send_keys("Abin3")
driver.find_element(By.ID,"umobile").send_keys("178782578748")
driver.find_element(By.ID,"sub_regbutton").click()
alert = driver.switch_to.alert
alert.accept()
alert_text = alert.text
print(alert_text)












