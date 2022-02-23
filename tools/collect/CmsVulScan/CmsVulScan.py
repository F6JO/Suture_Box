import sys
import threading
from modules.command import command
from  modules.function import *
from modules.Mo_Fun import *
from modules import globalVar as gl
from modules.banner import banner
from CmsPay.merge_pay import generate
print(banner())
# 初始化全局变量
gl._init()
class main():
    def __init__(self,url):
        # 初始化url
        url = Url_init(url)


        # 为全局变量赋值
        gl.set_value('url', url)
        gl.set_value('thread', int(ages.thread))
        gl.set_value('suo',threading.Lock())
        gl.set_value('save_path',ages.save_path)
        gl.set_value('proxies',proxies_init(ages.proxies))
        gl.set_value('out',int(ages.out))
        gl.set_value('URL',ages.URL)
        gl.set_value('md5_int',1)
        gl.set_value('re_int',1)
        gl.set_value('url_int',1)
        gl.set_value('md5pathlist',[])
        gl.set_value('md5md5list',[])
        gl.set_value('repathlist',[])
        gl.set_value('urlpathlist',[])
        gl.set_value('rerelist',[])
        gl.set_value('headers',{'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'})
        gl.set_value('ProxyError',1)
        gl.set_value('ReadTimeout',1)
        gl.set_value('ConnectTimeout',1)
        gl.set_value('ConnectionError',1)
        print(If_one()+times()+gl.get_value("color").yel_info()+gl.get_value("color").yellow(" CMS recognition of ")+gl.get_value("color").green(url)+gl.get_value("color").yellow(" in progress"))
        for i in Payload_Dict.keys():
            Transfer_device({i:Payload_Dict[i]},Clas.color)
        gl.clear()


if __name__ == '__main__':

    ages = command()
    if ages.gen:
        generate()
        sys.exit()
    Clas = CmsVLmap()
    Payload_Dict = Clas.Pay_init()
    if ages.save_path != None:
        save_init(ages.save_path)
    if ages.file == None:
        main(ages.url)
    else:
        file = open(ages.file,'r',encoding='utf-8')
        for i in file.readlines():
            url = i.replace("\n","")
            main(url)
    print("\n"+times()+gl.get_value("color").gre_ok()+gl.get_value("color").green(" CMS recognition is over"))