from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 初始化 WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 開啟範例網站
driver.get("https://www.yahoo.com")

# 查找頁面中的所有 <p> 標籤
elements = driver.find_elements(By.TAG_NAME, "p")

# 遍歷並打印每個 <p> 標籤的文字內容
for element in elements:
    print(element.text)
