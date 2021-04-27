from playwright.sync_api import sync_playwright
import time,random
from lxml import etree
import pymongo
def wques(context,page2,qlink):
    page2.goto(qlink)
    qcoll = db['ques']
    sid = ''
    url = ''
    created = ''
    updated = ''
    voteup = ''
    comment = ''
    content = ''
    excerpt = ''
    qid = ''
    qurl = ''
    title = ''
    qcreate = ''
    qupdated = ''
    aid = ''
    url_token = ''
    name = ''
    qdata = {  
             'sid': sid,  
             'url': url,  
             'created': created,  
             'updated': updated,
             'voteup': voteup,
             'comment': comment,
             'content': content,
             'excerpt': excerpt,
             'qid': qid,
             'qurl': qurl,
             'title': title,
             'qcreated': qcreated,
             'qupdated': qupdated,
             'aid': aid,
             'url_token': url_token,
             'name': name
            }  
    result = qcoll.insert_one(qdata)  
def wpage(context,page2,plink):
        page2.goto(plink)
        fstr = page2.content()
        html = etree.HTML(fstr)
        epath = '//h1/text()'
        title = html.xpath(epath)[0]
        epath = '//a[@class = "UserLink-link"]/@href'
        alink = html.xpath(epath)[0]
        epath = '//a[@class = "UserLink-link"]/text()'
        author = html.xpath(epath)[0]
        epath = '//button[@class="Button Button--plain"]/text()'
        hlink = html.xpath(epath)
        num = hlink[0].find(' ')
        t = hlink[0]
        f = int(num)
        voteup = t[:f]
        epath = '//div[@class="ContentItem-time"]/text()'
        ctime = html.xpath(epath)[0]
        pcoll = db['page']
        pdata = {
            'title': title,
            'alink': alink,
            'author': author,
            'voteup': voteup,
            'ctime': ctime,
            'content': fstr  
             }
        result = pcoll.insert_one(pdata)  
def getLink(html_str,plinks,qlinks):
    html = etree.HTML(html_str)
    epath = '//a/@href'
    hlink = html.xpath(epath)
    for i in range(0,len(hlink)):
        if hlink[i].find('/p/') > 0:
            plinks.append(hlink[i])
        if hlink[i].find('/question/') > 0:
            qlinks.append(hlink[i])
    #for i in range(1,len(links)):
    #    print(links[i])
    return plinks,qlinks
def npage(context,flink):
    page1 = context.new_page()
    page1.goto(flink)
    ts = page1.url.rfind('/')
    coll = page1.url[ts+1:]
    fn = './output/zhihu/'+coll+'-0.html'
    html_str = page1.content()
    with open(fn,'w+') as fo:
         fo.write(html_str)
    fo.close()
    plinks = []
    qlinks = []
    plinks,qlinks = getLink(html_str,plinks,qlinks)
    page2 = context.new_page()
    for j in range(0,len(plinks)):
        time.sleep(random.randrange(8,15))
        wpage(context,page2,plinks[j]) 
    for j in range(0,len(qlinks)):
        time.sleep(random(8,12))
        wques(context,page2,qlinks[j]) 
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
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
#print(mongo_client.server_info()) #判断是否连接成功
db = mongo_client['zhihu']
pcoll = db['page']
with sync_playwright() as playwright:
    run(playwright)