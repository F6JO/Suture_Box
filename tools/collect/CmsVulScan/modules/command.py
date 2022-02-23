import argparse

def command():

    parser = argparse.ArgumentParser(description="CmsVulScan")
    parser.add_argument("-u", dest='url', help='指定url，如：http://www.baidu.com')
    parser.add_argument("-f", dest='file', help='批量扫描，指定文本文件，一行一个url', default=None)
    parser.add_argument("-p", dest='proxies', help='设置代理，格式：http://127.0.0.1:8080', default=None)
    parser.add_argument("-o", dest='save_path', help='指定保存路径', default=None)
    parser.add_argument("-t", dest='thread', help='指定线程，默认20',default=20)
    parser.add_argument("-out", dest='out', help='指定超时时间，默认20',default=20)
    parser.add_argument("-gen", dest='gen', help='重新生成payload文件',action="store_true")
    parser.add_argument("-URL", dest='URL', help='设定是否进行url模块扫描（误报率高，建议扫不出东西时开启）',action="store_true")




    return parser.parse_args()