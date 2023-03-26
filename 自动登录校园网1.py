# _*_ coding : utf-8 _*_

import requests    # 用于向目标网站发送请求


url = 'http://172.30.255.42:801'#后面还有一长串，需要自己去操作，这里打码了，不然登录的就是我的校园网了    # 这行是你需要根据自己的情况修改的地方
response = requests.get(url).status_code  # 直接利用 GET 方式请求这个 URL 同时获取状态码
print("状态码{}".format(response))  # 打印状态码