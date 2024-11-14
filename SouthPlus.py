import time
from selenium import webdriver
import undetected_chromedriver as uc
import os

import subprocess


chrome_version = subprocess.check_output("google-chrome --version", shell=True).decode('utf-8')
version_main = int(chrome_version.split()[2].split('.')[0])
print(chrome_version,version_main)


#chrome_binary_path = os.environ['CHROME']
#chrome_driver_path = = os.environ['DRIVER']
SOUTHPLUS = os.environ['SOUTHPLUS']
UA = os.environ['UA']
cookies = {}
for cookie in SOUTHPLUS.split('; '):
    name, value = cookie.split('=', 1)  # 只分割第一个等号
    cookies[name] = value




#base_dir = os.path.dirname(os.path.abspath(__file__))
#chrome_binary_path = os.path.join(base_dir, '附加文件', 'chrome-win', 'chrome.exe')
#chrome_driver_path = os.path.join(base_dir, '附加文件', '运行数据','chromedriver.exe')


options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
#options.binary_location = chrome_binary_path  # 指定 Chrome 浏览器的可执行文件路径
options.add_argument("--disable-gpu")
options.add_argument("--disable-sync")
options.add_argument(f'--user-agent={UA}')
options.add_argument("disable-cache")#禁用缓存
options.add_argument("--headless")
#service = Service(executable_path=chrome_driver_path)
driver = uc.Chrome( options=options, version_main=version_main)  # 启动 Chrome 浏览器
#driver = webdriver.Chrome(service=service,options=options)  # 启动 Chrome 浏览器
driver.set_window_size(1000, 700)  # 设置浏览器窗口大小（宽度, 高度）
#driver.set_window_position(-850, 775)  # 设置浏览器窗口位置（x, y）
#driver.set_window_position(-850, 1355)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://www.south-plus.net/")
time.sleep(10)
for name, value in cookies.items():
    driver.add_cookie({'name': name, 'value': value})

try:
    driver.get("https://www.south-plus.net/plugin.php?H_name-tasks.html")
    print(driver.page_source)
    driver.execute_script("""document.getElementById("p_15").getElementsByTagName("a")[0].click();""")
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write("\n  ✔日常任务领取！")

except Exception as e:
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write(f"\n  ❗日常领取失败：{repr(e)}")
        print(e)


try:
    driver.get("https://www.south-plus.net/plugin.php?H_name-tasks-actions-newtasks.html.html")
    driver.execute_script("""document.getElementById("both_15").getElementsByTagName("a")[0].click();""")
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write("\n  ✔日常任务完成！")

except Exception as e:
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write(f"\n  ❗日常任务失败：{repr(e)}")
        print(e)
        print(repr(e))



driver.quit()
exit(0)
