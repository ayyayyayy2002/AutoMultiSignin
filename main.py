import subprocess
import requests
import sys
import os


UA = os.environ.get('UA')
BOTTOKEN = os.environ.get('BOTTOKEN')
USERID = os.environ.get('USERID')
SOUTHPLUS = os.environ.get('SOUTHPLUS')
ACGFUN = os.environ.get('ACGFUN')
EOHUT = os.environ['EOHUT']
VIKACG = os.environ['VIKACG']
V2EX = os.environ['V2EX']








with open("a.txt", "w", encoding='utf-8') as file:
    pass




# 检查 UA 是否存在，并打印
if UA:
    if SOUTHPLUS:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\nSouthplus签到结果：")
        try:
            # 运行 SouthPlus.py 脚本
            subprocess.run([sys.executable, 'SouthPlus.py'], check=True, capture_output=False)
        except Exception as e:
            #print(e)
            with open("a.txt", "a", encoding='utf-8') as file:
                file.write(f"\n  😅SouthPlus签到出错：\n{str(e)}")
    else:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\n  😢不进行Southplus签到")

    if ACGFUN:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\nAcgFun签到结果：")
        try:
            # 运行 SouthPlus.py 脚本
            subprocess.run([sys.executable, 'AcgFun.py'], check=True, capture_output=False)
        except Exception as e:
            #print(e)
            with open("a.txt", "a", encoding='utf-8') as file:
                file.write(f"\n  😅AcgFun签到出错：\n{str(e)}")

    else:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\n  😢不进行AcgFun签到")

    if EOHUT:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\nEoHut签到结果：")
        try:
            # 运行 SouthPlus.py 脚本
            subprocess.run([sys.executable, 'EoHut.py'], check=True, capture_output=False)
        except Exception as e:
            #print(e)
            with open("a.txt", "a", encoding='utf-8') as file:
                file.write(f"\n  😅EoHut签到出错：\n{str(e)}")
    else:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\n  😢不进行EoHut签到")

    '''
    if VIKACG:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\nVikACG签到结果：")
        try:
            # 运行 SouthPlus.py 脚本
            subprocess.run([sys.executable, 'VikACG.py'], check=True, capture_output=False)
        except Exception as e:
            #print(e)
            with open("a.txt", "a", encoding='utf-8') as file:
                file.write(f"\n  😅VikACG签到出错：\n{str(e)}")
    else:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\n  😢不进行VikACG签到")

    '''




    if V2EX:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\nV2EX签到结果：")
        try:
            # 运行 SouthPlus.py 脚本
            subprocess.run([sys.executable, 'V2EX.py'], check=True, capture_output=False)
        except Exception as e:
            #print(e)
            with open("a.txt", "a", encoding='utf-8') as file:
                file.write(f"\n  😅V2EX签到出错：\n{str(e)}")
    else:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\n  😢不进行V2EX签到")

















else:
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write("❗未设置UA，脚本拒绝执行")

if USERID:
    with open('a.txt', 'r', encoding='utf-8') as file:
        content = file.read()  # 读取文件内容

    # 发送消息到 Telegram
    url = f'https://api.telegram.org/bot{BOTTOKEN}/sendMessage'
    payload = {
        'chat_id': USERID,
        'text': content,
    }

    response = requests.post(url, data=payload)

else:
    exit(0)