from playwright.sync_api import sync_playwright
import time,random
def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://www.zhihu.com/signin?next=%2F
    page.goto("https://www.zhihu.com/signin?next=%2F")
    # Go to https://www.zhihu.com/
    page.goto("https://www.zhihu.com/")
    # Go to https://www.zhihu.com/people/stardust-23
    page.goto("https://www.zhihu.com/people/stardust-23")
    # Go to https://www.zhihu.com/people/stardust-23/collections
    
    # Open new page
    page1 = context.new_page()
    page1.goto('https://www.zhihu.com/collection/652463725')
    ts = page1.url.rfind('/')
    fn = page1.url[ts+1:]
    with open(fn,'w+') as fo:
         fo.write(page1.content())
    fo.close()

    # Click .Pagination button:nth-child(2)
    #page1.click(".Pagination button:nth-child(2)")
    # assert page1.url == "https://www.zhihu.com/collection/650873003?page=2"
    # Click .Pagination button:nth-child(4)
    #page1.click(".Pagination button:nth-child(4)")
    # assert page1.url == "https://www.zhihu.com/collection/650873003?page=3"
    # Click .Pagination button:nth-child(5)
    #page1.click(".Pagination button:nth-child(5)")
    # assert page1.url == "https://www.zhihu.com/collection/650873003?page=4"
    # Open new page
    #page2 = context.new_page()
    #page2.goto('https://zhuanlan.zhihu.com/p/365557490')
    # Click button:nth-child(6)
    #page1.click("button:nth-child(6)")
    # assert page1.url == "https://www.zhihu.com/collection/650873003?page=5"
    # Open new page
    #page3 = context.new_page()
    #page3.goto('https://www.zhihu.com/question/33578621/answer/451931102')
    # Open new page
    #page4 = context.new_page()
    #page4.goto('chrome://downloads/')
    # Close page
    #page4.close()
    # Click text=下一页
    while True:
        time.sleep(random.randrange(8,10))
        page1.click("text=下一页")
    # assert page1.url == "https://www.zhihu.com/collection/650873003?page=6"
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)