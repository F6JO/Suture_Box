# -*- coding: utf-8 -*-
import os
import platform
import sys
import threading


from System import globalVar as gl
from controller.controller import Repeater
from method.colour import Get_colour
from method.function import times,col,handle_exclude_list
from method.command import command
from method.banner import banner,Get_list
from method.set_ini import ini_init

print(banner())     # 打印随机banner
args = command()    # 获取参数

# 初始化全局变量
gl._init()

def main(target,modular,tool,info,single,exclude,output_file):

    # 将各常用变量注册为全局变量
    gl.set('root_path', os.getcwd())
    gl.set('target', target)
    gl.set('*',Get_colour().yel_info())
    gl.set('-',Get_colour().red_warn())
    gl.set('+',Get_colour().gre_ok())
    gl.set('time',times)
    gl.set('col',col)
    gl.set('info',info)
    gl.set('single',single)
    gl.set('lock',threading.Lock())
    gl.set('exclude',exclude)
    gl.set('JSFinder_mode','URL')   # JSFinder的输出匹配格式
    gl.set('output_file',output_file)
    gl.set('file_exis',True)
    gl.set('system',platform.system())  # 系统信息
    gl.set('python',sys.executable)  # 系统信息
    if not os.path.exists("./lock"): # 第一次执行初始化
        ini_init()                   # 创建配置文件
        open("./lock","w").close()
    Repeater(modular,tool)    # 进入中继模块



if __name__ == '__main__':
    target = args.target    # 目标
    modular = args.modular      # 模块
    tool = args.tool        # 工具
    output_file = args.output_file  # 保存文件
    single = args.single    # 是否关闭同时扫描
    info = args.info        # 是否打印info消息
    exclude = handle_exclude_list(args.exclude) # 排除指定工具
    print(Get_list()) if args.list else main(target,modular,tool,info,single,exclude,output_file) # 若有-list则打印列表
