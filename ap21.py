from playwright.sync_api import sync_playwright
import time,random
from lxml import etree
import pymongo
import json
def wques(context,page2,qlink,mongo_client):
    print('wques',qlink)
    #page2.goto(qlink)
    db = mongo_client['zhihu']
    qcoll = db['ques']
    pos2 = qlink.find('/question/')
    pos3 = qlink.find('/answer')
    q_id = qlink[pos2+10:pos3]
    items = 10
    start = 0
    end = 2
    for k in range(start,end):
        time.sleep(random.randrange(8,15))
        offset = k * items
    #print(offset)
        url = 'https://www.zhihu.com/api/v4/questions/'+q_id+'/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit='+str(items)+'&offset='+str(offset)+'&platform=desktop&sort_by=default'
        page2.goto(url)
        z = page2.content()
        #print(z)
        load_dict = z.json()
        for i in range(0,items):
            print(offset,i,q_id)
            sid = load_dict["data"][i]["id"]
            url = load_dict["data"][i]["url"]
            created = load_dict["data"][i]["created_time"]
            updated = load_dict["data"][i]["updated_time"]
            voteup = load_dict["data"][i]["voteup_count"]
            comment = load_dict["data"][i]["comment_count"]
            content = load_dict["data"][i]["content"]
            excerpt = load_dict["data"][i]["excerpt"]
            qid = load_dict["data"][i]["question"]["id"]
            qurl = load_dict["data"][i]["question"]["url"]
            title = load_dict["data"][i]["question"]["title"]
            qcreated = load_dict["data"][i]["question"]["created"]
            qupdated =  load_dict["data"][i]["question"]["updated_time"]
            aid = load_dict["data"][i]["author"]["id"]
            url_token = load_dict["data"][i]["author"]["url_token"]
            name = load_dict["data"][i]["author"]["name"]
        
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
def wpage(context,page2,plink,mongo_client):
        print('wpage ',plink)
        #print(mongo_client.server_info()) #判断是否连接成功
        db = mongo_client['zhihu']
        collection = db['page']
        print(plink)
        page2.goto(plink)
        fstr = page2.content()
        #print(fstr)
        html = etree.HTML(fstr)
        epath = '//h1/text()'
        title = html.xpath(epath)[0]
        epath = '//a[@class = "UserLink-link"]/@href'
        alink = 'https://'+html.xpath(epath)[0]
        epath = '//a[@class = "UserLink-link"]/text()'
        author = html.xpath(epath)[0]
        epath = '//button[@class="Button Button--plain"]/text()'
        hlink = html.xpath(epath)
        if len(hlink)>0:
            num = hlink[0].find(' ')
            t = hlink[0]
            f = int(num)
            voteup = t[:f]
        else:
            voteup = 0
        epath = '//div[@class="ContentItem-time"]/text()'
        if len(html.xpath(epath)[0]>0):
            ctime = html.xpath(epath)[0]
        else:
            ctime = ''
        pcoll = db['page']
        pos1 = plink.find('/p/')
        pid = plink[pos1+3:]
        url = page2.url
        pdata = {
            'pid': pid,
            'url' : url,
            'title': title,
            'alink': alink,
            'author': author,
            'voteup': voteup,
            'ctime': ctime,
            'content': fstr  
             }
        result = pcoll.insert_one(pdata)  
def getLink(html_str,plinks,qlinks):
    print('getlink',plinks,qlinks)
    html = etree.HTML(html_str)
    epath = '//a/@href'
    hlink = html.xpath(epath)
    for i in range(0,len(hlink)):
        if hlink[i].find('/p/') > 0:
            plinks.append('https://'+hlink[i][2:])
        if (hlink[i].find('/question/') > 0) and (hlink[i].find('/waiting') < 0):
            qlinks.append('https://'+hlink[i][2:])
    #for i in range(1,len(links)):
    #    print(links[i])
    return plinks,qlinks
def npage(context,flink,mongo_client):
    print('npage')
    page1 = context.new_page()
    page1.goto(flink)
    print('goto ',flink)
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
        print('sleep')
        time.sleep(random.randrange(8,15))
        wpage(context,page2,plinks[j],mongo_client)
        #print(plinks[j]) 
    for j in range(0,len(qlinks)):
        print('sleep')
        time.sleep(random.randrange(8,15))
        wques(context,page2,qlinks[j],mongo_client) 
        #print(qlinks[j])
    #comment api url
    #https://www.zhihu.com/api/v4/articles/79673343/root_comments?order=normal&limit=20&offset=0&status=open
def run(playwright):
    mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    #print(mongo_client.server_info()) #判断是否连接成功
    
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://www.zhihu.com/signin?next=%2F
    page.goto("https://www.zhihu.com/signin?next=%2F")
    # Go to https://www.zhihu.com/
    page.goto("https://www.zhihu.com/")
    time.sleep(random.randrange(8,15))
    print('sleep')
    # Go to https://www.zhihu.com/people/stardust-23/collections
    #page.goto("https://www.zhihu.com/people/stardust-23/collections")
    #flink = 'https://www.zhihu.com/collection/510656407'
    #flink = 'https://www.zhihu.com/collection/503653238'
    flink = 'https://www.zhihu.com/collection/510655767'
    npage(context,flink,mongo_client)
    
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