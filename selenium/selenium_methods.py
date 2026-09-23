from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Tarayıcının kendi kendine kapanmasını engelleyen ayar:
ayarlar = Options()
ayarlar.add_experimental_option("detach", True)

# Ayarları Chrome'a bağlayarak başlatıyoruz:
driver = webdriver.Chrome(options=ayarlar)

url = "https://www.instagram.com/"
driver.get(url)
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get(url + "selimemir_ocak")
driver.save_screenshot("instagram_screenshot.png")