import json
t = json.dumps([json.load(open('t.json')),json.load(open('t02.json'))])
print(t)
f = open('mg.json','a+')
f.write(t)
f.close()