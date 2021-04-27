from playwright.sync_api import sync_playwright
import time,random
from lxml import etree
def getLink(html_str,links):
    html = etree.HTML(html_str)
    epath = '//a/@href'
    hlink = html.xpath(epath)
    for i in range(0,len(hlink)):
        if hlink[i].find('/p/') > 0:
            plinks.append(hlink[i])
        if hlink[i].find('/question/') > 0:
            qlinks.append(hlink[i])
    for i in range(1,len(links)):
        print(links[i])
    return plinks,qlinks
def npage(context,flink):
    page1 = context.new_page()
    page1.goto(flink)
    ts = page1.url.rfind('/')
    fn = './output/zhihu/'+page1.url[ts+1:]+'-0.html'
    html_str = page1.content()
    with open(fn,'w+') as fo:
         fo.write(html_str)
    fo.close()
    plinks = []
    qlinks = []
    plinks,qlinks = getLinks(html_str,plinks,qlinks)
    #comment api url
    #https://www.zhihu.com/api/v4/articles/79673343/root_comments?order=normal&limit=20&offset=0&status=open
def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://www.zhihu.com/signin?next=%2F
    page.goto("https://www.zhihu.com/signin?next=%2F")
    # Go to https://www.zhihu.com/
    page.goto("https://www.zhihu.com/")
    # Go to https://www.zhihu.com/people/stardust-23/collections
    #page.goto("https://www.zhihu.com/people/stardust-23/collections")
    flink = 'https://www.zhihu.com/collection/510656407'
    npage(context,flink)
    
    #pagination xpath
    #for i in range(1,int(links[len(links)-2])):
    ##hlink = html.xpath("//div[@class='SelfCollectionItem-innerContainer']/a/@href")
    ##    for j in range(0,len(hlink)):
    ##        time.sleep(random.randrange(8,10))
    ##        page.click("text=下一页")
         
    
    
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)