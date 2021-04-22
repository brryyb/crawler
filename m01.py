import pymongo
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
#print(mongo_client.server_info()) #判断是否连接成功
db = mongo_client['zhihu']
coll = db['questions']
d = coll.find({'qid':32189846})
c = d.count()
print(d.next()['title'])