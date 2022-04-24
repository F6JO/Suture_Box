# -*- coding: utf-8 -*-
from method.function import lock_print,output
from System import globalVar as gl

# 将命令返回的每一行进行匹配输出
@lock_print
def vulmap(row):
    out = ''
    if '[+]' in row:
        print(gl.get('time')() + gl.get('+') + gl.get('col')('[vulmap]', 'yellow') + ' ' + gl.get('col')(
            row.split('[+] ')[1], 'cyan'))
        out = f"[vulmap] {row.split('[+] ')[1]}"
    elif '[?]' in row:
        print(gl.get('time')() + gl.get('+') + gl.get('col')('[vulmap]', 'yellow') + ' ' + gl.get('col')(
            row.split('[?] ')[1], 'cyan'))
        out = f"[vulmap] {row.split('[?] ')[1]}"
    elif '[-]' in row and gl.get('info'):
        print(gl.get('time')() + gl.get('*') + gl.get('col')('[vulmap]', 'yellow') + ' ' + gl.get('col')(
            row.split('[-] ')[1], 'cyan'))
    output(out)

@lock_print
def POC_bomber(row):
    if '[SUCCESS]' in row:
        print(gl.get('time')() + gl.get('+') + gl.get('col')('[POC_bomber]', 'yellow') + ' ' + gl.get('col')(
            row.split('检测到: ')[1], 'cyan'))
        output(f"[POC_bomber] {row.split('检测到: ')[1]}")
    elif '[INFO]' in row and gl.get('info'):
        print(gl.get('time')() + gl.get('*') + gl.get('col')('[POC_bomber]', 'yellow') + ' ' + gl.get('col')(
            row.split('[INFO]')[1], 'cyan'))



@lock_print
def nuclei(row):
    for i in row:
        i = i.replace('\n', '')
        if '[critical]' in i or '[high]' in i:
            print(gl.get('time')() + gl.get('+') + gl.get('col')('[nuclei]', 'yellow') + ' ' + gl.get('col')(
                i[i.find(' [')::], 'cyan'))
            output(f"[nuclei] {i[i.find(' [')::]}")
        elif '[info]' in i and gl.get('info'):
            print(gl.get('time')() + gl.get('*') + gl.get('col')('[nuclei]', 'yellow') + ' ' + gl.get('col')(
                i[i.find(' [')::], 'cyan'))
