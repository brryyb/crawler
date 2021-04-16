import json
items = 10
with open("answers01.json",'r') as load_f:
     load_dict = json.load(load_f)
     #print(load_dict)
     for i in range(0,items):
         sid = load_dict["data"][i]["id"]
         url = load_dict["data"][i]["url"]
         created = load_dict["data"][i]["created_time"]
         updated = load_dict["data"][i]["updated_time"]
         print(sid,url,created,updated)
     print(load_dict["data"][2]["excerpt"])
     