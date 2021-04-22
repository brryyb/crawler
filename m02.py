import pymongo
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
#print(mongo_client.server_info()) #判断是否连接成功
db = mongo_client['zhihu']
coll = db['questions']
d = coll.find({'qid':361477416})
c = d.count()
print(c)
#while (d.next()):
for i in d:
    #print(i,d.next()["excerpt"])
    print(i["excerpt"])
    #print(i,d.next()["title"])
    #把每一条数据都单独拿出来进行逐行的控制
    #print(d.next())
    #将游标数据取出来后，其实每行数据返回的都是一个［object BSON］型的内容
    #printjson(doc)
    #将游标获取的集合以JSON的形式显示
