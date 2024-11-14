from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time



COOKIE = ''
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
cookies = {}
if COOKIE:
    for cookie in COOKIE.split('; '):
        name, value = cookie.split('=', 1)  # 只分割第一个等号
        cookies[name] = value


chrome_binary_path = 'chrome-win\chrome.exe'
chrome_driver_path = 'chromedriver.exe'


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.binary_location = chrome_binary_path
options.add_argument("--disable-gpu")
options.add_argument("--disable-sync")
options.add_argument(f'--user-agent={UA}')
options.add_argument("disable-cache")
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)  # 启动 Chrome 浏览器
driver.set_window_size(1000, 700)  # 设置浏览器窗口大小（宽度, 高度）
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.get("https://baidu.com/")
for name, value in cookies.items():
    driver.add_cookie({'name': name, 'value': value})
time.sleep(10000)


driver.quit()
exit(0)
