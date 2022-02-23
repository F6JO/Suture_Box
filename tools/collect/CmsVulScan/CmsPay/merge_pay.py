import json
import os
import sys
import modules.function as fun
# sys.path.append('../')
import importlib
geshu = 0
def generate():
    """
        导入每个字典中的 run.py 并执行一遍重新生成每个的payload.txt
    """
    try:
        for i in os.listdir("Dict"):
            mode = "Dict." + i + ".run"
            datetime_module = importlib.import_module(mode)
        print(fun.times() + fun.col("[*] Payload file generated successfully", "yellow"))
    except Exception as err:
        print(fun.times() + fun.col("[-] The payload file does not exist. Use -gen True to generate the payload file", "red"))
        sys.exit()

    # 合并
    print(fun.times() + fun.col("[*] Merging payload files", "yellow"))
    try:
        NewPay = open("CmsPay/payload.txt", "w", encoding="utf-8")
        for i in os.listdir("Dict"):
            file = open("Dict/" + i + "/payload.txt", "r", encoding="utf-8")
            for a in file.readlines():
                if "\"url\": \"\"" in a:
                    continue
                NewPay.write(a)
            file.close()
        NewPay.close()
    except:
        print(fun.times() + fun.col("[-] Payload File merge failed", "red"))
        sys.exit()
    print(fun.times() + fun.col("[+] Payload file generated successfully", "green"))

def dete():

    print(fun.times()+fun.col("[*] Check whether the payload file exists","yellow"))
    if not os.path.exists("CmsPay/payload.txt"):
        print(fun.times()+fun.col("[-] Payload file does not exist", "red"))
        sys.exit()

# 去重
def Dr_list():
    jihe = set()
    file = open("CmsPay/payload.txt","r",encoding="utf-8")
    lis = file.readlines()
    file.close()
    for i in lis:
        i = i.replace("\n","")
        jihe.add(i)
    list_pay = []
    for i in jihe:
        list_pay.append(i)
    return [list_pay,len(lis)]



