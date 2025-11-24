from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 初始化 WebDriver 服務
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 開啟 Google 網站
driver.get("https://www.google.com")

# 顯示頁面標題
print(driver.title)
