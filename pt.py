from lxml import etree
with open('pt.html','r') as pf:
    fstr = pf.read()
    pf.close()
html = etree.HTML(fstr)
epath = '//h1/text()'
hlink = html.xpath(epath)
print(hlink[0])
epath = '//a[@class = "UserLink-link"]/@href'
hlink = html.xpath(epath)
print(hlink[0])
epath = '//a[@class = "UserLink-link"]/text()'
hlink = html.xpath(epath)
print(hlink[0])
epath = '//button[@class="Button Button--plain"]/text()'
hlink = html.xpath(epath)
print(hlink[0])
num = hlink[0].find(' ')
t = hlink[0]
#print(t[0,])
print(int(num)-1)
f = int(num)
print(t[:f])
epath = '//div[@class="ContentItem-time"]/text()'
hlink = html.xpath(epath)
print(hlink[0])