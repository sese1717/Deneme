from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")

input("Sayfayı kapatmak için terminalde Enter'a bas...")
driver.quit()