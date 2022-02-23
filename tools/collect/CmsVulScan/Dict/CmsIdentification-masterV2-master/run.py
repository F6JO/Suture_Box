
import json
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
def a():
    file = open("Dict/CmsIdentification-masterV2-master/data.json","r",encoding="utf-8")
    dakai = open("Dict/CmsIdentification-masterV2-master/payload.txt","w",encoding="utf-8")
    nr = file.read().lstrip("[").rstrip("]")
    nr1 = "{\"zidian\":["+nr+"]}"
    zidian = json.loads(nr1)
    for i in zidian["zidian"]:
        dakai.write(json.dumps(i)+"\n")


a()
