from lxml import etree
def getLink(html_str,plinks,qlinks):
    html = etree.HTML(html_str)
    epath = '//a/@href'
    hlink = html.xpath(epath)
    for i in range(0,len(hlink)):
        if hlink[i].find('/p/') > 0:
            plinks.append(hlink[i][2:])
        if (hlink[i].find('/question/') > 0) and (hlink[i].find('/waiting') < 0):
            qlinks.append(hlink[i][2:])
        #print(hlink[i].find('/waiting/'))
    return plinks,qlinks
fn = './output/zhihu/510656407-0.html'
with open(fn,'r') as fo:
     html_str = fo.read()
fo.close()
plinks = []
qlinks = []
plinks,qlinks = getLink(html_str,plinks,qlinks)
print(plinks,qlinks)