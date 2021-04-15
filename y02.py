import json
with open("answers01.json",'r') as load_f:
     load_dict = json.load(load_f)
     #print(load_dict)
     print(load_dict["data"][2]["excerpt"])
 #load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
 #print(load_dict)