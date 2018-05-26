import requests
import os
h1={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
a="http://tieba.baidu.com/f?kw=百度&ie=utf-8&pn={}"
url_list=[]
for i in range (1,1000):
    url_temp=a.format(i*50)
    url_list.append(url_temp)
i=0

for url in url_list:
    i+=1
    r=requests.get(url,headers=h1)
    if r.status_code == 200:
        filename="d:/第{}页.txt".format(i)
        f=open(filename,"w",encoding="utf-8")
        f.write(r.content.decode())
        f.close()
    else:
        break