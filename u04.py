#https://zhuanlan.zhihu.com/p/139390552
"""采用 python selenium 无头浏览器，爬取单个用户的所有回答数据并保存为表格文件。"""

from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

def start_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def get_answers_url(driver,url):
    driver.get(url)
    sleep(5)
    rlts = driver.find_elements_by_xpath('//*[@id="Profile-answers"]/div[2]//div/div/h2/div/a')   
    answers = [[rlt.text,rlt.get_attribute("href")] for rlt in rlts]
    return answers

def get_answers_text(driver,url):
    driver.get(url)
    sleep(5)
    rlt = driver.find_element_by_class_name('RichContent-inner')
    content = rlt.text
    rlt = driver.find_element_by_class_name("ContentItem-time")
    date = rlt.find_element_by_xpath(".//a/span").get_attribute("data-tooltip")
    rlt = driver.find_element_by_class_name("ContentItem-actions")
    upvote = rlt.find_element_by_xpath(".//span/button").get_attribute("aria-label")
    return [content,date,upvote]

driver = start_driver()
#url = "https://www.zhihu.com/people/haili-9-70/answers"
url = 'file:///home/axu/proj/craw/haili.html'
answers = get_answers_url(driver,url)
answers_dict = {}
#for i in range(len(answers)):
for i in range(5,8):
    answers_dict[i] = {}
    answers_dict[i]["title"] = answers[i][0]
    answers_dict[i]["url"] = answers[i][1]
    answers_dict[i]["content"] = get_answers_text(driver,answers[i][1])[0]
    answers_dict[i]["date"] = get_answers_text(driver,answers[i][1])[1]
    answers_dict[i]["upvote"] = get_answers_text(driver,answers[i][1])[2]
    answers_dict[i]["timestamp"] = str(datetime.now())[:-7]

df = pd.DataFrame(answers_dict).T
file = "./zhihu_answers_" + str(datetime.now().date()) + ".csv"
df.to_csv(file)