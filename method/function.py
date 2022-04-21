# -*- coding: utf-8 -*-
import copy
import os,re
import time
from functools import wraps

from System import globalVar as gl
from configparser import ConfigParser
import tqdm,inspect,contextlib

# 将信息打印在进度条上方
@contextlib.contextmanager
def redirect_to_tqdm():
    # Store builtin print
    old_print = print
    def new_print(*args, **kwargs):
        # If tqdm.tqdm.write raises error, use builtin print
        try:
            tqdm.tqdm.write(*args, **kwargs)
        except:
            old_print(*args, ** kwargs)

    try:
        # Globaly replace print with new_print
        inspect.builtins.print = new_print
        yield
    finally:
        inspect.builtins.print = old_print

# 读取ini文件
def read_ini_dict(title):
    conf = ConfigParser()  # 需要实例化一个ConfigParser对象
    # if gl.get('system') == 'Windows':
    #     path = gl.get('root_path')+'/tools/config_win.ini'
    # else:
    path = gl.get('root_path')+'/tools/config.ini'
    conf.read(path,"utf-8-sig")
    zidian = {}
    for i in conf.items(title):
        zidian[i[0]] = i[1]
    return zidian

# 获取工具路径
def Get_tool_path(path,gongju):
    if gongju == 'all':
        list = []
        for i in os.listdir(path):
            a = i.split('/')
            if '.' in a[-1]:
                pass
            else:
                if a[-1] not in gl.get('exclude'):
                    list.append(path + '/' + i)
        return list
    else:
        list = []
        list.append(path + '/' + gongju)
        return list

# 正则匹配判断目标为ip或url
def match_url_or_ip(ip):
    if len(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', ip)) != 0:
        return 'url'
    elif len(re.findall(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', ip)) != 0:
        return 'ip'
    else:
        print('请输入正确url或ip')

# 为字符串设置颜色
def col(str,col):
    if col == "green":
        return "\033[1;32;40m{}\033[0m".format(str)
    elif col == "red":
        return "\033[1;31;40m{}\033[0m".format(str)
    elif col == "yellow":
        return "\033[1;33;40m{}\033[0m".format(str)
    elif col == "cyan":
        return "\033[1;36;40m{}\033[0m".format(str)

# 获取当前时间字符串
def times():
    return col("["+time.strftime("%H:%M:%S", time.localtime())+"] ","cyan")



# 线程安全的装饰器
def lock_print(a):
    @wraps(a)
    def b(x):
        gl.get('lock').acquire()
        a(x)
        gl.get('lock').release()
    return b

# 写入文件
def output(row):
    if row != None and row != '':
        file = gl.get('output_file')
        if file != None:
            if gl.get('file_exis'):
                gl.set('file_exis', False)
                mode = 'w'
            else:
                mode = 'a'
            out = open(file, mode)
            out.write(f'[{time.strftime("%H:%M:%S",time.localtime())}] ' + row + '\n')
            out.close()

# 线程安全的输出
def Lprint(a):
    @wraps(a)
    def b(x):
        gl.get('lock').acquire()
        a(x)
        gl.get('lock').release()

    return b


# 获取dirmap返回的文件大小
def dirmap_size(a):
    b = re.findall('\[([0-9]{1,9}\.[0-9]{0,5}[k]?b)\]', a)[0]
    return b



# 判断目标是否为域名
def is_domain(a):
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False
    b = a.split('/')[2]
    c = b.split('.')
    ji = len(c)
    j = 0
    for i in c:
        i = i.replace(':',"")
        if is_number(i):
            j +=1
    if ji == j:
        return False
    else:
        return True


# 将排除的工具转换为列表
def handle_exclude_list(string):
    return string.replace(' ','').split(',')

# 线程安全的打印字符串
@Lprint
def lprint(a):
    print(a)