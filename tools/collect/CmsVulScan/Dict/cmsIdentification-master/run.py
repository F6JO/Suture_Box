import json
import os

def a():
    liebiao = os.listdir('Dict/cmsIdentification-master/yjcms')
    dakai = open("Dict/cmsIdentification-master/payload.txt","w",encoding="utf-8")
    for i in liebiao:
        file = open("Dict/cmsIdentification-master/yjcms/"+i,"r",encoding="utf-8")
        nr = file.readlines()
        file.close()
        for a in nr:
            zi = {}
            b = a.replace("\n","").replace(" ","")
            url,re,name = b.split("------")
            zi["url"] = url
            zi["re"] = re
            zi["name"] = name
            zi["md5"] = ""
            dakai.write(json.dumps(zi)+"\n")


def b():
    file = open("Dict/cmsIdentification-master/cms00.txt","r",encoding="utf-8")
    dakai = open("Dict/cmsIdentification-master/payload.txt","a",encoding="utf-8")
    for i in file.readlines():
        zi = {}
        a = i.replace("\n","")
        b = a.split(" ")
        zi["url"] = b[0]
        zi["re"] = ""
        zi["name"] = b[1]
        zi["md5"] = b[2]
        dakai.write(json.dumps(zi)+"\n")

def c():
    file = open("Dict/cmsIdentification-master/cms1.txt","r",encoding="utf-8")
    dakai = open("Dict/cmsIdentification-master/payload.txt","a",encoding="utf-8")
    zi = {}
    for i in file.readlines():
        a = i.replace("\n","")
        url,name = a.split(" ")
        zi[url] = name
    for i in zi.keys():
        zidian = {}
        zidian["url"] = i
        zidian["name"] = zi[i]
        zidian["re"] = ""
        zidian["md5"] = ""
        dakai.write(json.dumps(zidian)+"\n")

def d():
    file = open("Dict/cmsIdentification-master/data.json","r",encoding="utf-8")
    dakai = open("Dict/cmsIdentification-master/payload.txt","a",encoding="utf-8")
    nr = file.read()
    file.close()
    zidian = json.loads(nr.replace("[","{\"zidian\":[").replace("]","]}"))
    for i in zidian["zidian"]:
        dakai.write(json.dumps(i)+"\n")


a()
b()
c()
d()