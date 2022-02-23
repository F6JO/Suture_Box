
import requests
from modules import globalVar as gl
from modules.function import *

requests.logging.captureWarnings(True)



def md5_start(zidian):
    gl.get_value('suo').acquire()
    progress("md5", gl.get_value("md5_int"))
    gl.set_value("md5_int", gl.get_value("md5_int") + 1)
    gl.get_value('suo').release()
    url = gl.get_value("url")
    path = Path_init(zidian['url'])
    name = zidian['name']
    md5 = zidian['md5']
    try:
        if gl.get_value("proxies") != None:
            # print(type(gl.get_value("proxies")))
            requ = requests.get(url + path, verify=False, allow_redirects=False,timeout=gl.get_value("out"),
                                proxies=gl.get_value("proxies"),headers=gl.get_value("headers"))
            # print(requ.text)
        else:
            requ = requests.get(url + path, verify=False, allow_redirects=False, timeout=gl.get_value("out"),
                                headers=gl.get_value("headers"))
        code = requ.status_code
        if code == 200:
            if Get_Md5(requ.content) == md5:
                gl.get_value('suo').acquire()
                if md5 not in gl.get_value('md5md5list') or path not in gl.get_value('md5pathlist'):

                    print("\n"+times() + gl.get_value(
                        'color').gre_ok() + gl.get_value('color').green(
                        ' Using MD5 to discover the CMS in path ') + gl.get_value('color').yellow(
                        path) + ": " + gl.get_value(
                        'color').green(name))
                    save(url, path, "md5", name)
                    gl.get_value('md5pathlist').append(path)
                    gl.get_value('md5md5list').append(md5)
                gl.get_value('suo').release()
    except requests.exceptions.ProxyError:
        gl.get_value('suo').acquire()
        Error_print("ProxyError")
        gl.get_value('suo').release()
    except requests.exceptions.ReadTimeout:
        gl.get_value('suo').acquire()
        Error_print("ReadTimeout")
        gl.get_value('suo').release()
    except requests.exceptions.ConnectTimeout:
        gl.get_value('suo').acquire()
        Error_print("ConnectTimeout")
        gl.get_value('suo').release()
    except requests.exceptions.ConnectionError:
        gl.get_value('suo').acquire()
        Error_print("ConnectionError")
        gl.get_value('suo').release()


def re_start(zidian):
    gl.get_value('suo').acquire()
    progress("re", gl.get_value("re_int"))
    gl.set_value("re_int", gl.get_value("re_int") + 1)
    gl.get_value('suo').release()
    url = gl.get_value("url")
    path = Path_init(zidian['url'])
    name = zidian['name']
    re = zidian['re']
    try:
        if gl.get_value("proxies") != None:
            requ = requests.get(url + path, verify=False, allow_redirects=False, timeout=gl.get_value("out"),headers=gl.get_value("headers"),
                                proxies=gl.get_value("proxies"))
        else:
            requ = requests.get(url + path, verify=False, allow_redirects=False, timeout=gl.get_value("out"),headers=gl.get_value("headers"))
        code = requ.status_code
        if code == 200:
            if re in requ.text or re in headers_init(requ.headers):
                gl.get_value('suo').acquire()
                if path not in gl.get_value('repathlist') or re not in gl.get_value('rerelist'):

                    print("\n"+times() + gl.get_value(
                        'color').gre_ok() + gl.get_value('color').green(
                        ' Using RE to discover the CMS in path ') + gl.get_value('color').yellow(
                        path) + ": " + gl.get_value(
                        'color').green(name))
                    save(url, path, "re", name)
                    gl.get_value('repathlist').append(path)
                    gl.get_value('rerelist').append(re)
                gl.get_value('suo').release()
    except requests.exceptions.ProxyError:
        gl.get_value('suo').acquire()
        Error_print("ProxyError")
        gl.get_value('suo').release()
    except requests.exceptions.ReadTimeout:
        gl.get_value('suo').acquire()
        Error_print("ReadTimeout")
        gl.get_value('suo').release()
    except requests.exceptions.ConnectTimeout:
        gl.get_value('suo').acquire()
        Error_print("ConnectTimeout")
        gl.get_value('suo').release()
    except requests.exceptions.ConnectionError:
        gl.get_value('suo').acquire()
        Error_print("ConnectionError")
        gl.get_value('suo').release()

    # finally:
    #     gl.set_value('re_int',gl.get_value('re_int')+1)


def url_start(zidian):
    gl.get_value('suo').acquire()
    progress("url", gl.get_value("url_int"))
    gl.set_value("url_int", gl.get_value("url_int") + 1)
    gl.get_value('suo').release()
    url = gl.get_value("url")
    path = Path_init(zidian['url'])
    name = zidian['name']
    try:
        if gl.get_value("proxies") != None:
            requ = requests.get(url + path, verify=False, allow_redirects=False, timeout=gl.get_value("out"),headers=gl.get_value("headers"),
                                proxies=gl.get_value("proxies"))
        else:
            requ = requests.get(url + path, verify=False, allow_redirects=False, timeout=gl.get_value("out"),headers=gl.get_value("headers"))
        code = requ.status_code
        if code == 200:
            gl.get_value('suo').acquire()
            if path not in gl.get_value('urlpathlist'):

                print("\n"+times() + gl.get_value(
                    'color').gre_ok() + gl.get_value('color').green(
                    ' Using URL to discover the CMS in path ') + gl.get_value('color').yellow(
                    path) + ": " + gl.get_value(
                    'color').green(name))
                save(url, path, "url", name)
                gl.get_value('urlpathlist').append(path)

            gl.get_value('suo').release()

    except requests.exceptions.ProxyError:
        gl.get_value('suo').acquire()
        Error_print("ProxyError")
        gl.get_value('suo').release()
    except requests.exceptions.ReadTimeout:
        gl.get_value('suo').acquire()
        Error_print("ReadTimeout")
        gl.get_value('suo').release()
    except requests.exceptions.ConnectTimeout:
        gl.get_value('suo').acquire()
        Error_print("ConnectTimeout")
        gl.get_value('suo').release()
    except requests.exceptions.ConnectionError:
        gl.get_value('suo').acquire()
        Error_print("ConnectionError")
        gl.get_value('suo').release()

    # finally:
    #     gl.set_value('url_int',gl.get_value('url_int')+1)
