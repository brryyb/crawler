from playwright.sync_api import sync_playwright
import time,random
from lxml import etree
def npage(context,flink):
    page1 = context.new_page()
    page1.goto(flink)
    ts = page1.url.rfind('/')
    fn = './output/zhihu/'+page1.url[ts+1:]+'-0.html'
    html_str = page1.content()
    with open(fn,'w+') as fo:
         fo.write(html_str)
    fo.close()

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
    flink = 'https://www.zhihu.com/collection/664870672'
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