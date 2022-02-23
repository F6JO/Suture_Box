import json
import os

def run():
    liebiao = os.listdir('Dict/cms_identify-master')
    dakai = open("Dict/cms_identify-master/payload.txt","w",encoding="utf-8")
    for i in liebiao:
        if (".py" not in i) and (i != "payload.txt") and (i != "__pycache__"):
            file = open("Dict/cms_identify-master/"+i,"r",encoding="utf-8")
            nr = file.readlines()
            file.close()
            for a in nr:
                zi = {}
                b = a.replace("\n","")
                url,re,name = b.split("------")
                zi["url"] = url
                zi["re"] = re
                zi["name"] = name
                zi["md5"] = ""
                dakai.write(json.dumps(zi)+"\n")


run()