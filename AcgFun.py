from selenium import webdriver
import os


ACGFUN = os.environ['ACGFUN']
UA = os.environ['UA']
cookies = {}
for cookie in ACGFUN.split('; '):
    name, value = cookie.split('=', 1)  # 只分割第一个等号
    cookies[name] = value


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-gpu")
options.add_argument("--disable-sync")
options.add_argument(f'--user-agent={UA}')
options.add_argument("disable-cache")#禁用缓存
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.set_window_size(1000, 700)
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
