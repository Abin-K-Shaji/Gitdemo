import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"a[href*='shop]").click()
Products=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in Products :
    productName=product.find_element(By.XPATH,"/div/h4/a").text
    if productName=="Blackberry":
        product.find_element(By.XPATH,"/div/button").click()
driver.find_elements(By.CSS_SELECTOR,"a[class*='btn-primary']")
time.sleep(3)