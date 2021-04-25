from lxml import etree

def getLink(fname,epath,links):
    with open(fname) as f:
        html_str = f.read()
        f.close()
    #print(read_d)
    html = etree.HTML(html_str)
    #htext = html.xpath("//div['SelfCollectionItem-title']/a/text()")
    hlink = html.xpath(epath)
    #print(len(hlink),len(htext))
    #print(hlink,htext)
    #print(hlink[8],htext[8],len(hlink))
    for i in range(0,len(hlink)):
       #print(hlink[i].find('/collection/'))
       #if hlink[i].find('/collection/') > 0:
          #print(i,hlink[i])
       links.append(hlink[i])
          #print (i,len(hlink))

def plinks(links):
    ll = len(links)
    for i in range(0,ll):
        url = links[i]
    #if url.find('question'):
        print(i,url)

links = []
#class="Button PaginationButton PaginationButton-next Button--plain
#ContentItem-title
#epath = "//div['SelfCollectionItem-title']/a/@href"
##epath = "//div['CollectionDetailPageItem-innerContainer']/a/@href"
epath = "//h2/div/a/@href"
getLink('fd.html',epath,links)
plinks(links)
links = []
#xpath = "//a[text()='上一步']"
epath = "//*[contains(@class,'PaginationButton')]/text()"
getLink('f2.html',epath,links)
plinks(links)
#getLink('f3.html',epath,links)


    
    



    
