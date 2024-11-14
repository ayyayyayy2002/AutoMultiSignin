import time
from selenium import webdriver
import undetected_chromedriver as uc
import os

import subprocess

# 获取Chrome浏览器的版本号
chrome_version = subprocess.check_output("google-chrome --version", shell=True).decode('utf-8')
print(chrome_version)

import subprocess

# 获取Chrome浏览器的版本号
chrome_version = subprocess.check_output("chromium-browser --version", shell=True).decode('utf-8')
print(chrome_version)




