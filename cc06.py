import json
import pymongo
import requests
import time,random
#db connection
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
#print(mongo_client.server_info()) #判断是否连接成功
db = mongo_client['zhihu']
collection = db['questions']
#init para
items = 10
start = 0
end = 30
#q_id = '20894671'
#q_id = '30899950'
#q_id = '22292474'
#q_id = '37167038'
#q_id = '20532926'
#q_id = '24326030'
#q_id = '28361295'
#q_id = '35112627'
#q_id = '27353387'
#q_id = '41992632' 
#q_id = '21758700' 
#q_id = 20381470
#q_id = '36546814'
q_id = '27050272' 
#27353387
#20381470
#36546814
#27050272 3
fname = 'urllist.txt'
f = open(fname,'a+')
#init request 
HEADERS = {
    'Cookie':'',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
s = requests.session()
#loop -- read pages
for k in range(start,end):
    time.sleep(random.randrange(8,15))
    offset = k * items
    #print(offset)
    #print('page', i, 'num', offset)
    url = 'https://www.zhihu.com/api/v4/questions/'+q_id+'/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit='+str(items)+'&offset='+str(offset)+'&platform=desktop&sort_by=default'
    z = s.get(url,headers=HEADERS)
    f.write(url+'\r\n')
    load_dict = z.json()
    #read json data
    for i in range(0,items):
         print(offset,i)
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
         #print(sid,url,created,updated,voteup,comment,excerpt,name)
         answer = {  
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
         result = collection.insert_one(answer)  
f.close()

     
     