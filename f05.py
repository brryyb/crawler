from lxml import etree

def getLink(fname,links):
    with open(fname) as f:
        html_str = f.read()
        f.close()
    #print(read_d)
    html = etree.HTML(html_str)
    #htext = html.xpath("//div['SelfCollectionItem-title']/a/text()")
    hlink = html.xpath("//div['SelfCollectionItem-title']/a/@href")
    #print(len(hlink),len(htext))
    #print(hlink,htext)
    #print(hlink[8],htext[8],len(hlink))
    for i in range(0,len(hlink)):
       #print(hlink[i].find('/collection/'))
       if hlink[i].find('/collection/') > 0:
          #print(i,hlink[i])
          links.append(hlink[i])
          #print (i,len(hlink))
links = []
llink = ''
getLink('f.html',links)
getLink('f2.html',links)
getLink('f3.html',links)
#print(links)
for i in range(0,len(links)):
    print(i,links[i])
    llink = links[i]+'\r\n'+llink
fo = open('flink.txt','w')
fo.write(llink)
fo.close()
