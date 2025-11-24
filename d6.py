from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 啟動 Chrome
driver = webdriver.Chrome()

# 開 Google
driver.get("https://www.google.com")

# 執行 JavaScript（跳出 alert）
driver.execute_script("alert('Hello from Selenium!');")

time.sleep(3)  # 暫停一下讓你看到 alert
driver.quit()
