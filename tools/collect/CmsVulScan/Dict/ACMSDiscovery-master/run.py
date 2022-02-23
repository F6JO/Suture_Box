#-*-coding:UTF-8 -*-
import json

def ACMSDiscovery():
    a = open(r"Dict/ACMSDiscovery-master/data.txt","r",encoding="utf-8")
    b = a.read()
    a.close()
    c = b.replace(" ","").replace("[","{\"a\":[").replace("]","]}")
    liebiao = json.loads(c)["a"]
    dakai = open("Dict/ACMSDiscovery-master/payload.txt","w",encoding="utf-8")
    for i in liebiao:
        dakai.write(json.dumps(i)+"\n")


def b():
    file = open("Dict/ACMSDiscovery-master/file.txt","r",encoding="utf-8")
    liebiao = file.readlines()
    file.close()
    dakai = open("Dict/ACMSDiscovery-master/payload.txt","a",encoding="utf-8")
    for i in liebiao:
        zidian = {}
        a = i.replace("\n","")
        lujing,cms = a.split(" ")
        zidian["url"]=lujing
        zidian["name"]=cms
        zidian["re"]=""
        zidian["md5"]=""
        dakai.write(json.dumps(zidian)+"\n")

def c():
    file = open("Dict/ACMSDiscovery-master/md5.txt","r",encoding="utf-8")
    liebiao = file.readlines()
    file.close()
    dakai = open("Dict/ACMSDiscovery-master/payload.txt","a",encoding="utf-8")
    for i in liebiao:
        zidian = {}
        a = i.replace("\n","")
        b = a.rstrip(" ")
        url,name,md = b.split(" ")
        zidian["url"] = url
        zidian["name"] = name
        zidian["md5"] = md
        zidian["re"] = ""
        dakai.write(json.dumps(zidian)+"\n")


ACMSDiscovery()
b()
c()