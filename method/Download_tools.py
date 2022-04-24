import os
import stat
import sys
import threading
from System import globalVar as gl
import requests
from lxml import html
import tqdm
requests.logging.captureWarnings(True)


class Download():
    def __init__(self):
        self.proxies = gl.get("proxy")
        self.suo = threading.Lock()
        self.url = "https://github.com/F6JO/Suture_Box_tools"
        self.path_bu = "/tree/main/"
        self.dow_url = "https://raw.githubusercontent.com/F6JO/Suture_Box_tools/main/"

    def get_dir(self,do):
        dir_list = []
        try:
            fanhui = requests.get(do,verify=False,proxies=self.proxies)
        except:
            # print("xxxxxxx")
            # print(do)
            self.get_dir(do)
        else:
            # open("./lianxi.html","w").write(fanhui.text)
            xpath = html.etree.HTML(fanhui.text)
            div = xpath.xpath('/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[1]/div[2]/div[3]/div[1]/div')
            xp = "./div[2]/span/a/text()"
            start = 1
            if len(div) == 0:
                # print(1111)
                div = xpath.xpath(
                    '/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[1]/div[2]/include-fragment/div[2]/div[1]/div')
                xp = "./div[2]/span/a/text()"
                if len(div) == 0:
                    # print(22222)
                    div = xpath.xpath(
                        '/html/body/div[4]/div/main/div[2]/div/div/div[3]/include-fragment/div[2]/div/div')
                    xp = './div[2]/span/a/text()'
                    start = 2
                    if len(div) == 0:
                        # print(33333)
                        div = xpath.xpath('/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[3]/div/div')
                        xp = "./div[2]/span/a/text()"
                        start = 2
            # print(len(div))
            for i in div[start::]:
                aaa = i.xpath(xp)
                dir_list.append(aaa[0])
            return dir_list

    def download(self,mou,fen,tool,*patht):
        path =  mou + fen + tool
        a = ""
        for i in patht:
            if i == "":
                continue
            if a.endswith('/'):
                a += i
            else:
                a += fen +i
            if a[0] == "/" and a[1] == "/":
                a = a[1::]
        path += a
        try:
            req = requests.get(self.dow_url + path,verify=False,proxies=self.proxies)
        except:
            # print("ffffffff")
            # print(self.dow_url)
            self.download(mou,fen,tool,a)
        else:
            if req.status_code == 200:
                self.suo.acquire()
                self.save(path,req.content)
                self.suo.release()
            else:
                for i in self.get_dir(self.url + self.path_bu + path):
                    # print(threading.active_count())
                    if threading.active_count() >= 20:
                        self.download(mou ,fen,tool,a,i)
                    else:
                        thead = threading.Thread(target=self.download, args=[mou,fen,tool,a,i])
                        thead.start()
                        # download(mou ,fen,tool,a,i)

    def save(self,path,zijie):
        mulu = path.split("/")
        lujing = "./tools"
        if not os.path.exists("./tools"):
            os.mkdir(lujing)
        for i in mulu[0:-1]:
            lujing += "/"+i
            if not os.path.exists(lujing):
                os.mkdir(lujing)
        file = open("./tools/"+path,"wb")
        file.write(zijie)
        file.flush()
        file.close()
        os.chmod("./tools/"+path,stat.S_IRWXU|stat.S_IRWXO|stat.S_IRWXG)
        pbar.update(1)
        # print("./tools/"+path)

    def get_tool(self,tool):
        moud = self.get_dir(self.url)
        for i in moud:
            tools = self.get_dir(self.url + self.path_bu + i)
            if tool in tools:
                global pbar
                pbar = tqdm.tqdm(total=self.get_size(i,tool))
                pbar.set_description(tool)
                self.download(i , "/" , tool)
                break



    def get_size(self,mo,tool):
        urlinfo = f"https://raw.githubusercontent.com/F6JO/Suture_Box_tools/main/{mo}/info.xtx"
        qingqiu = requests.get(urlinfo,verify=False,proxies=self.proxies)
        for i in qingqiu.text.split("\n")[0:-1]:
            i = i.rstrip("   ")
            b = i.split("   ")
            if b[3] == tool:
                return int(b[2])

