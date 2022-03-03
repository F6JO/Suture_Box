# -*- coding: utf-8 -*-
import threadpool
from System import globalVar as gl
from System.exec_command import *
from System.command_proc import command_proc
from method.function import read_ini_dict,Get_tool_path,match_url_or_ip,lock_print,lprint,is_domain,redirect_to_tqdm
from method.call_tool_func.vulscan import *
from method.call_tool_func.collect import *
import tqdm
class Repeater():
    def __init__(self,mokuai,gongju):
        # 获取指定模块下的所有工具路径
        self.path = gl.get('root_path') + "/tools/" + mokuai
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

            # if gl.get('single'):
            #     list1 = []
            #     for i in tools_list:
            #         list1.append(gevent.spawn(start, i))
            #     self.jindu = tqdm.tqdm(total=len(list1))
            #     gevent.joinall(list1)
            # else:
            #     self.jindu = tqdm.tqdm(total=len(tools_list))
            #     for i in tools_list:
            #         start(i)

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
            self.jindu.update(1)
        #     lprint(gl.get('time')() + gl.get('*') + gl.get('col')(f'[{tool}]', 'yellow') + ' ' + gl.get('col')(
        # f'{tool} Running OK!', 'green'))
        else:
            pass








