import configparser
from System import globalVar as gl


def ini_init():
    config = configparser.ConfigParser()
    tools = {"POC_bomber":"vulscan",
             "vulmap":"vulscan",
             "nuclei":"vulscan",
             "dirmap":"collect",
             "dismap":"collect",
         "CmsVulScan":"collect",
         "JSFinder":"collect",
         "identYwaf":"collect",
         "TideFinger":"collect",
         "ksubdomain":"collect"}
    for tool,mode in tools.items():
        start_mode = ""
        start_file = ""
        target_mode = ""
        command_para = ""
        if tool == "POC_bomber":
            start_mode = gl.get("python")
            start_file = "pocbomber.py"
            target_mode = "url"
            command_para = "-t 5"
        elif tool == "vulmap":
            start_mode = gl.get("python")
            start_file = "vulmap.py"
            target_mode = "url"
            command_para = "-t 10"
        elif tool == "nuclei":
            if gl.get("system") == "Windows":
                start_file = "nuclei.exe"
            elif gl.get("system") == "Darwin":
                start_mode = "./"
                start_file = "nuclei_mac"
            else:
                start_mode = "./"
                start_file = "nuclei_linux"
            target_mode = "url"
        elif tool == "dirmap":
            start_mode = gl.get("python")
            start_file = "dirmap.py"
            target_mode = "url"
            command_para = "-t 10"
        elif tool == "dismap":
            if gl.get("system") == "Windows":
                start_file = "dismap.exe"
            elif gl.get("system") == "Darwin":
                start_mode = "./"
                start_file = "dismap_mac"
            else:
                start_mode = "./"
                start_file = "dismap_linux"
            target_mode = "url"
            command_para = "-t 1"
        elif tool == "CmsVulScan":
            start_mode = gl.get("python")
            start_file = "CmsVulScan.py"
            target_mode = "url"
            command_para = "-t 10"
        elif tool == "JSFinder":
            start_mode = gl.get("python")
            start_file = "JSFinder.py"
            target_mode = "url"
        elif tool == "identYwaf":
            start_mode = gl.get("python")
            start_file = "identYwaf.py"
            target_mode = "url"
        elif tool == "TideFinger":
            start_mode = gl.get("python")
            start_file = "TideFinger.py"
            target_mode = "url"
            command_para = "-d 1"
        elif tool == "ksubdomain":
            if gl.get("system") == "Windows":
                start_file = "ksubdomain.exe"
            elif gl.get("system") == "Darwin":
                start_mode = "./"
                start_file = "ksubdomain_mac"
            else:
                start_mode = "./"
                start_file = "ksubdomain_linux"
            target_mode = "domain"
            command_para = "-api"
        name = mode+"/"+tool
        config.add_section(mode+"/"+tool)
        config[name]['start_mode'] = start_mode
        config[name]['start_file'] = start_file
        config[name]['target_mode'] = target_mode
        config[name]['command_para'] = command_para
    #
    with open('./tools/config.ini', 'w') as configfile:
        config.write(configfile)