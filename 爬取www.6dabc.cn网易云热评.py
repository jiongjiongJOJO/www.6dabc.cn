import re
import requests
import time

def zhuaqu(n):
    data = requests.get('https://www.6dabc.cn/wy/'+str(n)+'.html').text
    data = data.replace('\n','')
    data = data.replace('\t','')
    data = data.replace(' ','')
    pattern = '''description(.*)pubDate'''
    result = re.compile(pattern).findall(data)
    return result
time1 = time.time()
f = open('E:\\Users\\JOJO\\Desktop\\result.txt','a',encoding='utf-8')
for i in range(2,1192):
    s = zhuaqu(i)
    if(len(s)==0):
        continue
    f.write(s[0]+'\n')
    print('已完成：'+str(i-1)+'/1190')
f.close()
time2 = time.time()
print('用时： %f 秒' % (time2-time1))
