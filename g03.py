from lxml import etree
from selenium import webdriver
import time,random
def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    #options.add_argument("--no-sandbox") # linux only
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
    })
    return driver
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
       if hlink[i].find('/collection/') > 0:
          #print(i,hlink[i])
          links.append(hlink[i])
          #print (i,len(hlink))


links = []
epath = "//div['SelfCollectionItem-title']/a/@href"
getLink('f.html',epath,links)
getLink('f2.html',epath,links)
getLink('f3.html',epath,links)

driver = getDriver()
ll = len(links)
for i in range(5,7):
    time.sleep(random.randrange(5,10))
    print(i,links[i])
    url = links[i]
    if url.find('question'):
       print(i,url)
       driver.get(url)
       alink = driver.find_element_by_class_name("ContentItem-title")
       alink.click()



    
