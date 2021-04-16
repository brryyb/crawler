import json
import pymongo
items = 10
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
print(mongo_client.server_info()) #判断是否连接成功
db = mongo_client['zhihu']
collection = db['questions']
with open("answers01.json",'r') as load_f:
     load_dict = json.load(load_f)
     #print(load_dict)
     for i in range(0,items):
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
         print(sid,url,created,updated,voteup,comment,excerpt,name)
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


     
     