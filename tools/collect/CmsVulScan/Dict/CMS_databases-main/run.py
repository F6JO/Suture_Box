import json
import os



def a():
    file1 = open(r"Dict/CMS_databases-main/a.txt","r",encoding="utf-8")
    file = file1.readlines()
    file1.close()

    baocun = open(r"Dict/CMS_databases-main/payload.txt","w",encoding="utf-8")
    jishu = 0
    for i in file:
        if jishu == 0:
            jishu += 1
            continue
        zidian = {}
        a = i.replace("\n", "")
        b = a.split(" fenge123321  ")
        zidian["url"] = b[1]
        zidian["re"] = ""
        zidian["name"] = b[0]
        zidian["md5"] = b[2]

        baocun.write(json.dumps(zidian)+"\n")

def b():
    file1 = open(r"Dict/CMS_databases-main/b.txt", "r",encoding="utf-8")
    file = file1.readlines()
    file1.close()
    baocun = open(r"Dict/CMS_databases-main/payload.txt", "a",encoding="utf-8")
    jishu = 0
    for i in file:
        if jishu == 0:
            jishu += 1
            continue
        zidian = {}
        a = i.replace("\n", "")
        b = a.split(" fenge123321 ")
        zidian["url"] = b[1]
        zidian["re"] = b[2]
        zidian["name"] = b[0]
        zidian["md5"] = ""
        #
        baocun.write(json.dumps(zidian) + "\n")


a()
b()