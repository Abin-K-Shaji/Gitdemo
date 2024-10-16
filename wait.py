import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
results=driver.find_elements(By.CSS_SELECTOR,"div[class='products'] div")
time.sleep(3)
count=len(results)
print(count)
for result in results:
    result.find_element(By.XPATH,"div/button").click()
time.sleep(3)



