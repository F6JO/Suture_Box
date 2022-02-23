import json
import modules.function as fun
import threadpool
import CmsPay.merge_pay as Get_list
from modules.requ import *
from modules import globalVar as gl

class CmsVLmap:
    def __init__(self):
        Get_list.dete()
        self.GET = Get_list.Dr_list()
        self.PayLoads = self.GET[0]
        self.Len = self.GET[1]
        from modules.color import Get_color
        gl.set_value('color',Get_color())
        self.color = gl.get_value('color')
        self.Md5 = []
        self.Re = []
        self.Url = []
    def Pay_init(self):
        for i in self.PayLoads:
            try:
                dic = json.loads(i)
            except:
                print(fun.times()+fun.col("[-] Error: ensure that the last line of Dict/test/payload.txt is null to regenerate payloads","red"))
                exit()
            if dic["md5"] == "" and dic["re"] == "":
                self.Url.append(dic)
            elif dic["md5"] != "":
                self.Md5.append(dic)
            elif dic["re"] != "":
                self.Re.append(dic)
        if len(self.PayLoads) == (len(self.Md5) + len(self.Re) + len(self.Url)):
            print(fun.times()+fun.col("[*]"+" All Payload {} duplicate removal {}".format(self.Len,len(self.Md5)+len(self.Re)+len(self.Url)),"yellow"))
            print(fun.times()+fun.col("[+] Payload load the success","green"))
        else:
            print(fun.times() + fun.col("[-] Payload Loading failure", "red"))

        return {'md5':self.Md5,'url':self.Url,'re':self.Re}


def Transfer_device(pay_dict,color):
    thread = gl.get_value("thread")
    key = ''
    for i in pay_dict.keys():
        key = i

    if key == "md5":
        gl.set_value("MD5_zong", len(pay_dict['md5']))
        print(fun.times() + color.yel_info() + color.yellow(" Scanning by MD5 mode......"))
        pool = threadpool.ThreadPool(thread)  # 线程数
        xiancheng = threadpool.makeRequests(md5_start, pay_dict['md5'])
        for i in xiancheng:
            pool.putRequest(i)
        pool.wait()
    elif key == "re":
        gl.set_value("RE_zong", len(pay_dict['re']))
        print("\n"+fun.times() + color.yel_info() + color.yellow(" Scanning by RE mode......"))
        pool = threadpool.ThreadPool(thread)  # 线程数
        xiancheng = threadpool.makeRequests(re_start, pay_dict['re'])
        for i in xiancheng:
            pool.putRequest(i)
        pool.wait()

    elif key == "url":
        if gl.get_value("URL"):
            gl.set_value("URL_zong",len(pay_dict['url']))
            print("\n"+fun.times() + color.yel_info() + color.yellow(" Scanning by URL mode......"))
            pool = threadpool.ThreadPool(thread)  # 线程数
            xiancheng = threadpool.makeRequests(url_start, pay_dict['url'])
            for i in xiancheng:
                pool.putRequest(i)
            pool.wait()



if __name__ == '__main__':
    CmsVLmap()



