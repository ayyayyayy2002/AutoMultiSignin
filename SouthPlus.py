import time
from selenium import webdriver
import undetected_chromedriver as uc
import os




import os

chrome_path = "/usr/bin/google-chrome"
chromium_path = "/usr/bin/chromium-browser"

if os.path.exists(chrome_path):
    print("已安装 Chrome")
elif os.path.exists(chromium_path):
    print("已安装 Chromium")
else:
    print("未安装 Chrome 或 Chromium")

import subprocess

# 获取Chrome浏览器的版本号
chrome_version = subprocess.check_output("google-chrome --version", shell=True).decode('utf-8')
print(chrome_version)

import subprocess

# 获取Chrome浏览器的版本号
chrome_version = subprocess.check_output("chromium-browser --version", shell=True).decode('utf-8')
print(chrome_version)




