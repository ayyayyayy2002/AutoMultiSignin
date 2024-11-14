from selenium import webdriver
import os









#chrome_binary_path = os.environ['CHROME']
#chrome_driver_path = = os.environ['DRIVER']
ACGFUN = os.environ['ACGFUN']
UA = os.environ['UA']
cookies = {}
for cookie in ACGFUN.split('; '):
    name, value = cookie.split('=', 1)  # 只分割第一个等号
    cookies[name] = value



base_dir = os.path.dirname(os.path.abspath(__file__))
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
#driver = webdriver.Chrome(service=service,options=options)  # 启动 Chrome 浏览器
#driver.set_window_position(-850, 775)  # 设置浏览器窗口位置（x, y）
#driver.set_window_size(1000, 700)  # 设置浏览器窗口大小（宽度, 高度）
#driver.set_window_position(-850, 1355)
driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.get("https://acgfun.moe/")
for name, value in cookies.items():
    driver.add_cookie({'name': name, 'value': value})

try:
    driver.get("https://acgfun.moe/")
    driver.execute_script("document.getElementById('k_misign_topb').querySelector('a').click();")
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write("\n  ✔签到成功！")

except Exception as e:
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write(f"\n  ❗签到失败：{repr(e)}")
        print(e)


driver.quit()
exit(0)
