import json
 
name_emb = {'a':'1111','b':'2222','c':'3333','d':'4444'} 
emb_filename = ('./emb_json.json')  

jsObj = json.dumps(name_emb)    

with open(emb_filename, "w") as f:  
    f.write(name_emb)  
    f.close()  

print(name_emb)
print(jsObj)
 
print(type(name_emb))
print(type(jsObj))

