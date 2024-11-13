import subprocess
import requests
import os













with open("a.txt", "w", encoding='utf-8') as file:
    pass
UA = os.environ.get('UA')
BOTTOKEN = os.environ.get('BOTTOKEN')
USERID = os.environ.get('USERID')
SOUTHPLUS = os.environ.get('SOUTHPLUS')
ACGFUN = os.environ.get('ACGFUN')
EOHUT = os.environ['EOHUT']

# 检查 UA 是否存在，并打印
if UA:

    if SOUTHPLUS:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\nSouthplus签到结果：")
        try:
            # 运行 SouthPlus.py 脚本
            subprocess.run(['python', 'SouthPlus.py'], check=True, capture_output=False)
        except Exception as e:
            print(e)
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
            subprocess.run(['python', 'AcgFun.py'], check=True, capture_output=False)
        except Exception as e:
            print(e)
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
            subprocess.run(['python', 'VikACG.py'], check=True, capture_output=False)
        except Exception as e:
            print(e)
            with open("a.txt", "a", encoding='utf-8') as file:
                file.write(f"\n  😅EoHut签到出错：\n{str(e)}")
    else:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\n  😢不进行EoHut签到")























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