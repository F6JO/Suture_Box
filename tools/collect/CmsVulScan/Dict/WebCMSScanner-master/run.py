import json


def a():
    file = open("Dict/WebCMSScanner-master/data.json","r",encoding="utf-8")
    zidian = json.loads(file.read().replace("[","{\"zidian\":[").replace("]","]}"))
    file.close()
    dakai = open("Dict/WebCMSScanner-master/payload.txt","w",encoding="utf-8")
    for i in zidian["zidian"]:
        dakai.write(json.dumps(i)+"\n")



a()