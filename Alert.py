import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)
driver.find_element(By.ID,"name").send_keys("hello")
driver.find_element(By.ID,"alertbtn").click()
alerts =driver.switch_to.alert
alt=alerts.text
print(alt)
alerts.accept()


