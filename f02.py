#
import requests
from lxml import etree

#url1 = 'https://book.douban.com/tag/%E6%97%A5%E6%9C%AC%E6%96%87%E5%AD%A6?start=0&type=T/'
url = 'https://www.zhihu.com/people/stardust-23/collections'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
response = requests.get(url, headers=headers)
html_str = response.content.decode()
html = etree.HTML(html_str)
#创建xpath列表
#html_name = html.xpath("//ul[@class='subject-list']/li")
html_name = html.xpath("//div[@class='Collections-mainColumn']")
#//div['SelfCollectionItem-title']
htext = html.xpath("//div['SelfCollectionItem-title']/a/text()")
hlink = html.xpath("//div['SelfCollectionItem-title']/a/@href")
print(hlink,htext)
#for li in html_name:
#    item = {}
#    #获取到每一个li下的书籍名字，并去除多余的\n
#    item['name'] = li.xpath('./div[2]/h2/a/text()')[0].replace("\\n", " ").strip()
#    print(item)