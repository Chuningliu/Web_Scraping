import json
with open ('Task5.json','r') as f:
    j=json.load(f)
dic={}
i=0
count=0
while  i<len(j):
    if j[i]['language']=='English':
        count=count+1
        dic['english']=count
    i=i+1
with open ("Task6.json","w") as f:
    json.dump(dic,f,indent=4 )