from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import subprocess
import os




chrome_version = subprocess.check_output("google-chrome --version", shell=True).decode('utf-8')
version_main = int(chrome_version.split()[2].split('.')[0])
print(chrome_version,version_main)
VIKACG = os.environ['VIKACG']
UA = os.environ['UA']
cookies = {}
for cookie in VIKACG.split('; '):
    name, value = cookie.split('=', 1)  # 只分割第一个等号
    cookies[name] = value
options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-gpu")
options.add_argument("--disable-sync")
options.add_argument(f'--user-agent={UA}')
options.add_argument("disable-cache")
options.add_argument("--headless")
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
