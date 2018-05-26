import requests
import json
url = "https://fanyi.baidu.com/basetrans"
h1 = {'User-Agent':'Mozilla/5.0 (iPhone 84; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.8.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1'}
str = input("请输入要翻译的中文：")
d1 = {'from':'zh','to':'en','query':str}
r = requests.post(url,data=d1,headers=h1).content.decode()

print(r)

#print(r.content.decode())

 #a = r.content.decode()
result = json.loads(r)
print(result)
 #print("翻译后的结果为：",result['trans'][0]['dst'])
print(r.json()['trans_result']['data'][0]['dst'])