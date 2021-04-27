from lxml import etree
import pymongo
with open('pt.html','r') as pf:
    fstr = pf.read()
    pf.close()
html = etree.HTML(fstr)
epath = '//h1/text()'
hlink = html.xpath(epath)
print(hlink[0])
title = hlink[0]
epath = '//a[@class = "UserLink-link"]/@href'
hlink = html.xpath(epath)
print(hlink[0])
alink = hlink[0]
epath = '//a[@class = "UserLink-link"]/text()'
hlink = html.xpath(epath)
print(hlink[0]) 
author = hlink[0]
epath = '//button[@class="Button Button--plain"]/text()'
hlink = html.xpath(epath)
print(hlink[0])
num = hlink[0].find(' ')
t = hlink[0]
#print(t[0,])
print(int(num)-1)
f = int(num)
print(t[:f])
voteup = t[:f]
epath = '//div[@class="ContentItem-time"]/text()'
hlink = html.xpath(epath)
print(hlink[0])
ctime = hlink[0]
#db connection
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
#print(mongo_client.server_info()) #判断是否连接成功
db = mongo_client['zhihu']
collection = db['page']
page = {
    'title': title,
    'alink': alink,
    'author': author,
    'voteup': voteup,
    'ctime': ctime  
     }
result = collection.insert_one(page)  