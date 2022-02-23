# -*- coding: utf-8 -*-
from System import globalVar as gl


# 对每个工具执行的命令添加必要的参数
def command_proc(comm, tool):
    if tool == 'vulmap':
        comm = comm + f' -u {gl.get("target")} --debug'
    elif tool == 'POC_bomber':
        comm = comm + f' -u {gl.get("target")}'
    elif tool == 'nuclei':
        comm = comm + f' -u {gl.get("target")} -silent -nc'
    elif tool == 'dirmap':
        comm = comm + f' -lcf -i {gl.get("target")}'
    elif tool == 'dismap':
        comm = comm + f' -url {gl.get("target")}'
    elif tool == 'CmsVulScan':
        comm = comm + f' -u {gl.get("target")}'
    elif tool == 'JSFinder':
        comm = comm + f' -u {gl.get("target")}'
    elif tool == 'identYwaf':
        comm = comm + f' {gl.get("target")}'
    elif tool == 'TideFinger':
        comm = comm + f' -u {gl.get("target")}'
    elif tool == 'ksubdomain':
        comm = comm + f' -d {gl.get("target").split("/")[2].split(".")[-2] + "."+gl.get("target").split("/")[2].split(".")[-1]} -silent'
    return comm