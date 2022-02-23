import json

file = open("Dict/gwhatweb-master/data.json","r",encoding="utf-8")
a = file.read().replace("[","{\"zidian\":[").replace("]","]}")
file.close()
zidian = json.loads(a)

dakai = open("Dict/gwhatweb-master/payload.txt","w",encoding="utf-8")
for i in zidian["zidian"]:
    dakai.write(json.dumps(i)+"\n")