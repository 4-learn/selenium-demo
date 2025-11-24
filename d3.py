from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 設定為無頭模式
options = webdriver.ChromeOptions()
options.add_argument("headless")

# 初始化 WebDriver 並應用選項
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")

# 顯示頁面標題
print(driver.title)
