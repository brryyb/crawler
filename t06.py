from lxml import etree
fname = 'ft01.html'
with open(fname) as f:
    html_str = f.read()
    f.close()
    #print(read_d)
    html = etree.HTML(html_str)
    #epath = "//*[@id="root"]/div/main/div/div[1]/div[2]/div[2]/div[3]/div/div/h2"
    #epath = 'ContentItem ArticleItem'
    #epath = '//h2[@class="ContentItem-title"]/a/@href'
    #epath = '//div[@class="ContentItem ArticleItem"]/div/h2/a/@href'
    epath = '//a/@href'
    hlink = html.xpath(epath)
    links = []
    for i in range(0,len(hlink)):
        if hlink[i].find('/p/') > 0:
            links.append(hlink[i])
        if hlink[i].find('/question/') > 0:
            links.append(hlink[i])
    for i in range(1,len(links)):
        print(links[i])
    