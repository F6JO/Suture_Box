# -*- coding: utf-8 -*-
import argparse

def command():

    parser = argparse.ArgumentParser(description="Suture_Box")
    target = parser.add_argument_group("target")
    target.add_argument("-u", dest='target', help='指定url，如：http://www.baidu.com')

    modular = parser.add_argument_group("modular")
    modular.add_argument("-m", dest='modular', help='设置调用的模块，vulscan(漏洞扫描)/collect(信息收集)，默认信息收集', default='collect')
    modular.add_argument("-t", dest='tool', help='指定单个调用的工具,如: -t vulmap，默认 all 全部调用', default='all')
    modular.add_argument("-x", dest='exclude', help='设置排除调用的工具,使用逗号隔开，如: -x vulmap,dismap',default='')

    modular = parser.add_argument_group("download")
    modular.add_argument("-d", dest='down', help='要下载的工具或者模块，如 -d vulscan 或 -d vulmap 或 -d all', default=None)
    modular.add_argument("-p", dest='proxy', help='设置代理，格式: 127.0.0.1:7890', default=None)

    other = parser.add_argument_group("other")
    other.add_argument("-o", dest='output_file', help='指定保存路径', default=None)
    other.add_argument("-single", dest='single', help='设定此参数后将依次运行工具，而不是同时运行', action="store_false")
    other.add_argument("-info", dest='info', help='设定是否打印info信息，默认关闭', action="store_true")
    other.add_argument("-list", dest='list', help='打印所有集成的工具信息', action="store_true")


    demo = parser.add_argument_group("examples")
    demo.add_argument(action='store_false',
                     dest="python3 -m pip install -r requirements.txt\n  "
                          "python3 suturebox.py -p 127.0.0.1 -d all\n  "
                          "python3 suturebox.py -p 127.0.0.1 -d vulscan\n  "
                          "python3 suturebox.py -p 127.0.0.1 -d vulmap\n  "
                          "python3 suturebox.py -u https://127.0.0.1 -m vulscan\n  "
                          "python3 suturebox.py -u https://127.0.0.1 -m vulscan -t vulmap\n  "
                          "python3 suturebox.py -u https://127.0.0.1 -m vulscan -x vulmap,nuclei\n  "
                          "python3 suturebox.py -u https://127.0.0.1 -m vulscan -x vulmap,nuclei -info -single")
    return parser.parse_args()