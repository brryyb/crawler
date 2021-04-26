from playwright.sync_api import sync_playwright
import time,random
from lxml import etree
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
    page.goto("https://www.zhihu.com/people/stardust-23/collections")
    #pagination xpath
    html_str = page.content()
    epath = "//*[contains(@class,'PaginationButton')]/text()"
    html = etree.HTML(html_str)
    links = html.xpath(epath)
    ts = page.url.rfind('/')
    for i in range(1,int(links[len(links)-2])):
        fn = './output/zhihu/'+page.url[ts+1:]+str(i)+'.html'
        with open(fn,'w+') as fo:
             fo.write(html_str)
        fo.close()
        links = []
        hlink = html.xpath("//div['SelfCollectionItem-title']/a/@href")
        for k in range(0,len(hlink)):
            if hlink[i].find('/collection/') > 0:
               links.append(hlink[i])
        for j in range(0,len(links)):
            
        time.sleep(random.randrange(8,10))
        page.click("text=下一页")
         
    
    
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)