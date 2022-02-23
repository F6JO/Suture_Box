import json

file = open("Dict/hexman-scaner-master/cmslist1.json","r",encoding="utf-8")
# file = open("./cmslist1.json","r",encoding="utf-8")
nr = file.read()
file.close()
zidian = json.loads(nr)
file1 = open("Dict/hexman-scaner-master/payload.txt","w",encoding="utf-8")
for i in zidian:
    file1.write(json.dumps(i)+"\n")
file1.close()