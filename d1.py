from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 自動安裝和管理 WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 開啟 Google 網站
driver.get("https://www.google.com")

# 顯示網頁標題
print(driver.title)

# 保持瀏覽器開啟
while True:
    pass
