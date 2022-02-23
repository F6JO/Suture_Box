# -*- coding: utf-8 -*-
import argparse

def command():

    parser = argparse.ArgumentParser(description="Suture_Box")
    parser.add_argument("-u", dest='target', help='指定url，如：http://www.baidu.com')
    parser.add_argument("-m", dest='moude', help='设置调用的模块，vulscan(漏洞扫描)/collect(信息收集)，默认信息收集', default='collect')
    parser.add_argument("-t", dest='tool', help='指定单个调用的工具,如: -t vulmap，默认 all 全部调用', default='all')
    parser.add_argument("-o", dest='output_file', help='指定保存路径', default=None)
    parser.add_argument("-x", dest='exclude', help='设置排除调用的工具,使用逗号隔开，如: -x vulmap,dismap',default='')
    parser.add_argument("-single", dest='single', help='设定此参数后将依次运行工具，而不是同时运行', action="store_false")
    parser.add_argument("-info", dest='info', help='设定是否打印info信息，默认关闭', action="store_true")
    parser.add_argument("-list", dest='list', help='打印所有集成的工具信息', action="store_true")
    return parser.parse_args()