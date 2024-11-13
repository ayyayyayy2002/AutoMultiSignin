from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import os








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


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
#options.binary_location = chrome_binary_path  # 指定 Chrome 浏览器的可执行文件路径
options.add_argument("--disable-gpu")
options.add_argument("--disable-sync")
options.add_argument(f'--user-agent={UA}')
options.add_argument("disable-cache")#禁用缓存
options.add_argument("--headless")
#service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(options=options)  # 启动 Chrome 浏览器
#driver = webdriver.Chrome(service=service,options=options)  # 启动 Chrome 浏览器
driver.set_window_size(1000, 700)  # 设置浏览器窗口大小（宽度, 高度）
#driver.set_window_position(-850, 775)  # 设置浏览器窗口位置（x, y）
#driver.set_window_position(-850, 1355)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://www.south-plus.net/")
for name, value in cookies.items():
    driver.add_cookie({'name': name, 'value': value})

try:
    driver.get("https://www.south-plus.net/plugin.php?H_name-tasks.html")
    daily = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="p_15"]/a/img'))
    )
    daily.click()
    # 创建一个名为a.txt的空文件
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write("\n  ✔日常任务领取！")

except Exception as e:
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write("\n  ❗日常领取失败！")
        print(e)


try:
    driver.get("https://www.south-plus.net/plugin.php?H_name-tasks-actions-newtasks.html.html")
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="both_15"]/a/img'))
    )
    element.click()
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write("\n  ✔日常任务完成！")

except Exception as e:
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write("\n  ❗日常任务失败！")
        print(e)



driver.quit()
exit(0)
