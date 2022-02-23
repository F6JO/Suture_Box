import json


def a():
    file = open("Dict/whaweb-master/cms.txt","r",encoding="utf-8")
    liebiao = file.readlines()
    file.close()
    dakai = open("Dict/whaweb-master/payload.txt","w",encoding="utf-8")
    for i in liebiao:
        zidian = {}
        i = i.replace("\n","")
        if ("范例" in i) or i == "":
            continue
        url,re,name = i.split("------")
        zidian["url"] = url
        zidian["re"] = re
        zidian["name"] = name
        zidian["md5"] = ""
        dakai.write(json.dumps(zidian)+"\n")





a()