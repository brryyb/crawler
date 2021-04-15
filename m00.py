import pymongo
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
print(mongo_client.server_info()) #判断是否连接成功
db = mongo_client['zhihu']
collection = db['questions']
student = {  
    'id': '20170101',  
    'name': 'Jordan',  
    'age': 20,  
    'gender': 'male'  
}  
result = collection.insert_one(student)  
print(result)  
print(result.inserted_id) 