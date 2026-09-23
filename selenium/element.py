from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.trendyol.com/samsung/galaxy-a16-128-gb-4-gb-ram-siyah-cep-telefonu-samsung-turkiye-garantili-p-881465224?boutiqueId=689770&merchantId=968"
driver.get(url)

# Eskisi: driver.find_element_by_class_name("product-title variant-pdp") -> PATLAR
# Yenisi (Doğru olan):
title = driver.find_element(By.CLASS_NAME, "product-title").text

print(title)

driver.close()