import hashlib
import sys
import time
from modules import globalVar as gl
# from tqdm import tqdm

start = 1
def col(str,col):
    if col == "green":
        return "\033[1;32;40m{}\033[0m".format(str)
    elif col == "red":
        return "\033[1;31;40m{}\033[0m".format(str)
    elif col == "yellow":
        return "\033[1;33;40m{}\033[0m".format(str)
    elif col == "cyan":
        return "\033[1;36;40m{}\033[0m".format(str)

def times():
    return col("["+time.strftime("%H:%M:%S", time.localtime())+"] ","cyan")

def Url_init(url):
    if url.endswith('/'):
        return url.rstrip('/')
    else:
        return url

def Path_init(path):
    if not path.startswith('/'):
        return '/'+path
    else:
        return path

def Get_Md5(str):
    my_md5 = hashlib.md5()  # 获取一个MD5的加密算法对象
    my_md5.update(str)  # 得到MD5消息摘要
    my_md5_Digest = my_md5.hexdigest()  # 以16进制返回消息摘要，32位
    return my_md5_Digest


def headers_init(head):
    str = ''
    keys = head.keys()
    for i in keys:
        str += i+":"+head[i]+"\n"
    return str

def save_init(path):
    open(path,"w",encoding="utf-8").close()


def save(url,path,str,name):
    if gl.get_value("save_path") != None:
        file = open(gl.get_value("save_path"),"a",encoding="utf-8")
        file.write(str+": "+url+": "+path+": "+name+"\n")
        file.close()

def proxies_init(str):
    if str != None:
        xieyi, daili = str.split('://')
        if gl.get_value("url").startswith("https"):
            return {"https":daili}
        else:
            return {"http":daili}
    else:
        return str



def Error_print(err):
    if err == "ProxyError":
        Error = gl.get_value(
            'color').red_warn() + gl.get_value(
            'color').red(" Target rejected, please check agent")
        print("\r", end="")
        print(" "*30+Error,"* {}".format(col(gl.get_value("ProxyError"),"red"))+" "*21, end="")
        gl.set_value("ProxyError",gl.get_value("ProxyError")+1)
        sys.stdout.flush()
    elif err == "ReadTimeout":
        Error = gl.get_value(
            'color').red_warn() + gl.get_value(
            'color').red(" The response timed out. Try adjusting the -out parameter")
        print("\r", end="")
        print(" "*30+Error, "* {}".format(col(gl.get_value("ReadTimeout"), "red")), end="")
        gl.set_value("ReadTimeout", gl.get_value("ReadTimeout") + 1)
        sys.stdout.flush()
    elif err == "ConnectTimeout":
        Error = gl.get_value(
            'color').red_warn() + gl.get_value(
            'color').red(" The response timed out. Try adjusting the -out parameter")
        print("\r", end="")
        print(" "*30+Error, "* {}".format(col(gl.get_value("ConnectTimeout"), "red")), end="")
        gl.set_value("ConnectTimeout", gl.get_value("ConnectTimeout") + 1)
        sys.stdout.flush()
    elif err == "ConnectionError":
        Error = gl.get_value(
            'color').red_warn() + gl.get_value(
            'color').red(" Failed to connect to this website")
        print("\r", end="")
        print(" "*30+Error, "* {}".format(col(gl.get_value("ConnectionError"), "red"))+" "*23, end="")
        gl.set_value("ConnectionError", gl.get_value("ConnectionError") + 1)
        sys.stdout.flush()


def progress(mod,ge):
    global nr, zong
    if mod == "md5":
        nr = " MD5: "
        zong = gl.get_value("MD5_zong")
    elif mod == "url":
        nr = " URL: "
        zong = gl.get_value("URL_zong")
    elif mod == "re":
        nr = " RE: "
        zong = gl.get_value("RE_zong")
    print("\r", end="")
    print(times()+ gl.get_value(
            'color').yel_info()+gl.get_value(
            'color').yellow(nr + "{}/{} ".format(ge,zong)), end="")
    sys.stdout.flush()

def If_one():
    global start
    if start == 1:
        start += 1
        return ""
    else:
        return "\n"
# def Progress_bar(name,geshu):
#     for i in tqdm(range(geshu), desc=name, ncols=80):
#         if name == 'md5':
#             while True:
#                 if gl.get_value('md5_int'):
#                     pass

if __name__ == '__main__':
    print(times())