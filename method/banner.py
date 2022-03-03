# -*- coding: utf-8 -*-
from method.function import col as color
import random

# 随机获取banner
import prettytable

banner_1 = color(r""" 
   _____       __                     ____            
  / ___/__  __/ /___  __________     / __ )____  _  __
  \__ \/ / / / __/ / / / ___/ _ \   / __  / __ \| |/_/
 ___/ / /_/ / /_/ /_/ / /  /  __/  / /_/ / /_/ />  <  
/____/\__,_/\__/\__,_/_/   \___/  /_____/\____/_/|_|                                                  
""","yellow")

banner_2 = color(r'''
   ____     __                 ___          
  / __/_ __/ /___ _________   / _ )___ __ __
 _\ \/ // / __/ // / __/ -_) / _  / _ \\ \ /
/___/\_,_/\__/\_,_/_/  \__/ /____/\___/_\_\ 

 ''',"green")


banner_3 = color(r'''
  _____       _                    ____            
 / ____|     | |                  |  _ \           
| (___  _   _| |_ _   _ _ __ ___  | |_) | _____  __
 \___ \| | | | __| | | | '__/ _ \ |  _ < / _ \ \/ /
 ____) | |_| | |_| |_| | | |  __/ | |_) | (_) >  < 
|_____/ \__,_|\__|\__,_|_|  \___| |____/ \___/_/\_\
                                                   
''',"red")



banner_4 = color(r'''
 ____        _                    ____            
/ ___| _   _| |_ _   _ _ __ ___  | __ )  _____  __
\___ \| | | | __| | | | '__/ _ \ |  _ \ / _ \ \/ /
 ___) | |_| | |_| |_| | | |  __/ | |_) | (_) >  < 
|____/ \__,_|\__|\__,_|_|  \___| |____/ \___/_/\_\
                                                  
''',"cyan")



def banner():
    o_o = random.choice(range(4))
    if o_o == 0:
        return banner_1
    elif o_o == 1:
        return banner_2
    elif o_o == 2:
        return banner_3
    elif o_o == 3:
        return banner_4


# 工具详细列表
def Get_list():
    row = prettytable.PrettyTable()
    row.field_names = ['Method', "Tool", 'By', "Url", "Info"]
    row.add_row(['Collect', "dismap", 'zhzyker', 'https://github.com/zhzyker/dismap',
                 '快速识别 Web 指纹信息，定位资产类型。辅助红队快速定位目标资产信息，辅助蓝队发现疑似脆弱点'])
    row.add_row(['Collect', "dirmap", 'H4ckForJob', 'https://github.com/H4ckForJob/dirmap',
                 '一个高级web目录、文件扫描工具，功能将会强于DirBuster、Dirsearch、cansina、御剑。'])
    row.add_row(['Collect', "identYwaf", 'stamparm', 'https://github.com/stamparm/identYwaf', 'WAF识别工具'])
    row.add_row(['Collect', "JSFinder", 'Threezh1', 'https://github.com/Threezh1/JSFinder',
                 'JSFinder是一种用于从网站上的JS文件中快速提取URL和子域的工具'])
    row.add_row(['Collect', "ksubdomain", 'knownsec', 'https://github.com/knownsec/ksubdomain', '无状态子域名爆破工具'])
    row.add_row(['Collect', "TideFinger", 'TideSec', 'https://github.com/TideSec/TideFinger',
                 'TideFinger——指纹识别小工具，汲取整合了多个web指纹库，结合了多种指纹检测方法，让指纹检测更快捷、准确。'])
    row.add_row(['Collect', "CmsVulScan", 'F6JO', 'https://github.com/F6JO/CmsVulScan',
                 'cms识别工具，用于识别网站使用的cms，收集了github上多个扫描工具的指纹'])
    row.add_row(['Vulscan', "vulmap", 'zhzyker', 'https://github.com/zhzyker/vulmap',
                 'Vulmap 是一款 web 漏洞扫描和验证工具, 可对 webapps 进行漏洞扫描, 并且具备漏洞验证功能'])
    row.add_row(['Vulscan', "POC-bomber", 'tr0uble-mAker', 'https://github.com/tr0uble-mAker/POC-bomber',
                 '利用大量高威胁poc/exp快速获取目标权限，用于渗透和红队快速打点'])
    row.add_row(['Vulscan', "nuclei", 'projectdiscovery', 'https://github.com/projectdiscovery/nuclei',
                 '基于简单的基于YAML的DSL的快速可定制漏洞扫描器'])
    return row
