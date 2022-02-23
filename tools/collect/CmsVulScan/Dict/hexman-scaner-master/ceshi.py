import json

file = open("./payload.txt","r")
for i in file.readlines():
    zidian = json.loads(i)
    print(zidian)