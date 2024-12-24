from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc




COOKIE = ""
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
cookies = {}
if COOKIE:
    for cookie in COOKIE.split('; '):
        name, value = cookie.split('=', 1)  # 只分割第一个等号
        cookies[name] = value
chrome_binary_path = 'chrome-win\chrome.exe'
chrome_driver_path = 'chromedriver.exe'


version_main = 89



options = uc.ChromeOptions()
options.binary_location = chrome_binary_path
#options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-gpu")
options.add_argument("--disable-sync")
options.add_argument(f'--user-agent={UA}')
options.add_argument("disable-cache")
#options.add_argument("--headless")
driver = uc.Chrome( options=options, version_main=version_main)  # 启动 Chrome 浏览器
driver.get("https://www.vikacg.com/post")
for name, value in cookies.items():
    driver.add_cookie({'name': name, 'value': value})

try:
    driver.get("https://www.vikacg.com/wallet/mission")
    page_source = driver.page_source

    # 打印网页源码
    WebDriverWait(driver, 20, 1).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[5]/div[2]'))
    ).click()
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write("\n  ✔签到成功！")

except (Exception,TimeoutException) as e:
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write(f"\n  ❗签到失败：{repr(e)}")
        print(e)







driver.quit()
exit(0)
