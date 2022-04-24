# -*- coding: utf-8 -*-
import os
import sys
import threading
import time

import threadpool
from System import globalVar as gl
from System.exec_command import *
from System.command_proc import command_proc
from method.function import read_ini_dict,Get_tool_path,match_url_or_ip,lock_print,lprint,is_domain,redirect_to_tqdm,if_tool_ex
from method.call_tool_func.vulscan import *
from method.call_tool_func.collect import *
from method.Download_tools import Download
import tqdm
class Repeater():
    def __init__(self,mokuai,gongju):
        # 获取指定模块下的所有工具路径
        self.path = gl.get('root_path') + "/tools/" + mokuai
        no_tool = if_tool_ex(self.path,gongju,gl.get(f"{mokuai}_tools"))
        if not no_tool[0]:

            for i in no_tool[1]:
                lprint(gl.get('time')() + gl.get('-') + gl.get('col')(f'Please install the tool ', 'yellow') +
                       gl.get('col')(i, 'red'))
            sys.exit(0)
        tools_list = Get_tool_path(self.path,gongju)
        thread = 1
        # 判断是否同时扫描
        if gl.get('single'):
            thread = len(tools_list)

        # 开启线程，几个工具几个协程
        def start(i):
            a = i.split('/')
            # 读取配置文件中所有数据
            dict = read_ini_dict(a[-2] + '/' + a[-1])
            # 执行命令中转
            self.exec(i,dict,i[i.rindex('/')+1::])

        with redirect_to_tqdm():
            self.jindu = tqdm.tqdm(total=len(tools_list))
            pool = threadpool.ThreadPool(thread)
            threads = threadpool.makeRequests(start, tools_list)
            for i in threads:
                pool.putRequest(i)
            pool.wait()

    def exec(self,path,dict,tool):
        # 对要执行的工具和命令字符串进行处理
        start_mode = dict['start_mode']
        if start_mode != "" and start_mode != "./":
            start_mode = start_mode + " "
        start_file = dict['start_file']
        target_mode = dict['target_mode']
        command_para = ' '+dict['command_para']
        # 判断目标格式是否与设定的格式相同
        if match_url_or_ip(gl.get('target')) == target_mode or (tool == 'ksubdomain' and is_domain(gl.get('target'))):
            lprint(gl.get('time')() + gl.get('*') + gl.get('col')(f'[{tool}]', 'yellow') + gl.get('col')(f' {tool} starts running', 'green'))
            # 有些工具无法用迭代器回显，所以单独执行
            # print(f"cd {path} && " + command_proc(start_mode  + start_file + command_para,tool))
            if tool == 'nuclei' or tool == 'ksubdomain':
                result = nuclei_cms(f"cd {path} && " + command_proc(start_mode  + start_file + command_para,tool))
                eval(tool)(result)
            elif tool == 'dismap':
                open(f'{path}/output.txt','w').close()
                dismap_cms(f"cd {path} && " + command_proc(start_mode  + start_file + command_para,tool))
                file = open(f'{path}/output.txt','r')
                eval(tool)(file.readlines())
                file.close()
            else:
                # 判断系统设置编码
                if gl.get('system') == 'Windows':
                    code = 'gbk'
                else:
                    code = 'utf8'
                # 执行命令
                result = external_cmd(f"cd {path} && " + command_proc(start_mode  + start_file + command_para,tool),code)
                while True:
                    try:
                        # 读取执行命令后的回显，并进入执行函数处理
                        eval(tool)(result.__next__())
                    except StopIteration:
                        break
                    except Exception as err:
                        lprint(err)
                        exit()
            # lprint(gl.get('time')() + gl.get('+') + gl.get('col')(tool, 'yellow') +
            #        gl.get('col')(" is OK", 'cyan'))
            self.jindu.update(1)
        #     lprint(gl.get('time')() + gl.get('*') + gl.get('col')(f'[{tool}]', 'yellow') + ' ' + gl.get('col')(
        # f'{tool} Running OK!', 'green'))
        else:
            pass

def dow_rep(down):
    if down != None:
        Dow = Download()
        if down == "all":
            for i in gl.get("collect_tools"):
                if if_thread():
                    Dow.get_tool(i)
            for i in gl.get("vulscan_tools"):
                if if_thread():
                    Dow.get_tool(i)
        elif down == "collect":
            for i in gl.get("collect_tools"):
                if if_thread():
                    Dow.get_tool(i)
        elif down == "vulscan":
            for i in gl.get("vulscan_tools"):
                if if_thread():
                    Dow.get_tool(i)

        elif down in gl.get("collect_tools") or down in gl.get("vulscan_tools"):
            Dow.get_tool(down)
        else:
            lprint(gl.get('time')() + gl.get('-') + gl.get('col')(f'There are no ', 'yellow') +
                   gl.get('col')(down, 'red') +
                   gl.get('col')(f' tools available for download', 'yellow'))
        sys.exit(0)


def if_thread():
    while True:
        if threading.active_count() == 2 or threading.active_count() == 1:
            return True
        else:
            time.sleep(1)


