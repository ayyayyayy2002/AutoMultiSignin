import undetected_chromedriver as uc
import subprocess
import time
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
driver.set_window_size(1000, 700)  # 设置浏览器窗口大小（宽度, 高度）
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.get("https://www.vikacg.com/post")
time.sleep(10)
for name, value in cookies.items():
    driver.add_cookie({'name': name, 'value': value})

try:
    driver.get("hhttps://www.vikacg.com/wallet/mission")
    page_source = driver.page_source

    # 打印网页源码
    print(page_source)
    driver.execute_script("""document.querySelector('.btn.inline.bg-gradient-info.btn-sm').click();""")
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write("\n  ✔签到成功！")

except Exception as e:
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write(f"\n  ❗签到失败：{repr(e)}")
        print(e)





driver.quit()
exit(0)
