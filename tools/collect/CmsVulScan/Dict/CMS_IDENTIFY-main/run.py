import json


def a():
    file = open("Dict/CMS_IDENTIFY-main/CMS_FINGER.json","r",encoding="utf-8")
    zidian = json.loads(file.read())
    file.close()
    liebiao = []
    for i in zidian.keys():
        for a in zidian[i].keys():
            if a == "md5":
                for x in zidian[i][a].keys():
                    zi = {}
                    zi["url"] = x
                    zi["md5"] = zidian[i][a][x]
                    zi["name"] = i
                    zi["re"] = ""
                    liebiao.append(zi)
            if a == "keyword":
                for x in zidian[i][a].keys():
                    zi = {}
                    zi["url"] = x
                    zi["md5"] = ""
                    zi["name"] = i
                    zi["re"] = zidian[i][a][x]
                    liebiao.append(zi)
    dakai = open("Dict/CMS_IDENTIFY-main/payload.txt","w",encoding="utf-8")
    for i in liebiao:
        dakai.write(json.dumps(i)+"\n")




a()