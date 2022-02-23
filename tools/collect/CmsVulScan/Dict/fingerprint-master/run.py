import json


def a():
    file = open("Dict/fingerprint-master/cms.json","r",encoding="utf-8")
    zidian = json.loads(file.read())
    file.close()
    dakai = open("Dict/fingerprint-master/payload.txt","w",encoding="utf-8")
    for i in zidian:
        zidian = {}
        zidian["name"] = i["tag"]
        zidian["url"] = i["url"]
        zidian["re"] = i["pattern"]
        zidian["md5"] = i["md5"]
        dakai.write(json.dumps(zidian)+"\n")




a()