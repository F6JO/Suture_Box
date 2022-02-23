# -*- coding: utf-8 -*-
from method.function import lock_print, dirmap_size,output
from System import globalVar as gl

# 将命令返回的每一行进行匹配输出
@lock_print
def dirmap(row):
    if '[200]' in row:
        nr = row.split('[200]')[1]
        size = dirmap_size(nr)
        lis = nr.split(size)
        print(gl.get('time')() + gl.get('+') + gl.get('col')('[dirmap]', 'yellow') + ' ' + gl.get('col')(
            lis[0], 'cyan') + gl.get('col')(
            size, 'yellow') + gl.get('col')(
            lis[1], 'cyan'))
        output('[dirmap] ' + lis[0] + size + lis[1])

@lock_print
def dismap(row):
    for i in row:
        i = i.replace('\n', '')
        if '[+] ' in i:
            print(gl.get('time')() + gl.get('+') + gl.get('col')('[dismap]', 'yellow') + ' ' + gl.get('col')(
                i.split('[+] ')[1], 'cyan'))
            output('[dismap] ' + i.split('[+] ')[1])
        elif '[-]' in i and gl.get('info'):
            print(gl.get('time')() + gl.get('*') + gl.get('col')('[dismap]', 'yellow') + ' ' +
                  gl.get('col')(i.split('[-] ')[1], 'cyan'))

@lock_print
def CmsVulScan(row):
    if '[+] Using' in row:
        sc = row.split('[+] ')[1].split(': ')
        print(gl.get('time')() + gl.get('+') + gl.get('col')('[CmsVulScan]', 'yellow') + ' ' + gl.get('col')(
            sc[0] + ': ', 'cyan') + gl.get('col')(
            sc[1], 'red'))
        output('[CmsVulScan] ' + sc[0] + ': ' + sc[1])
    elif '[*]' in row and gl.get('info'):
        print(gl.get('time')() + gl.get('*') + gl.get('col')('[CmsVulScan]', 'yellow') + ' ' + gl.get('col')(
            row.split('[*] ')[1], 'cyan'))


@lock_print
def JSFinder(row):
    if 'Find ' not in row and 'url:' not in row:
        print(gl.get('time')() + gl.get('+') + gl.get('col')('[JSFinder]', 'yellow') + ' ' + gl.get('col')(
            '[' + gl.get('JSFinder_mode') + ']', 'yellow') + ' ' + gl.get('col')(row, 'cyan'))
        output(f'[JSFinder] [{gl.get("JSFinder_mode")}] {row}')
    elif row.split(' ')[-1] == 'URL:':
        gl.set('JSFinder_mode', 'URL')
    elif row.split(' ')[-1] == 'Subdomain:':
        gl.set('JSFinder_mode', 'Subdomain')
    else:
        pass


@lock_print
def identYwaf(row):
    out = ''
    if '[x]' in row:
        print(gl.get('time')() + gl.get('+') + gl.get('col')('[identYwaf]', 'yellow') + ' ' + gl.get('col')(
            '[Not Waf]', 'green') + ' ' + gl.get('col')(
            row.split('x] ')[1], 'cyan'))
        out = f'[identYwaf] [Not Waf] {row.split("x] ")[1]}'
    elif '[+]' in row:
        print(gl.get('time')() + gl.get('+') + gl.get('col')('[identYwaf]', 'yellow') + ' ' + gl.get('col')(
            '[Waf!]', 'green') + ' ' + gl.get('col')(
            row.split('+] ')[1], 'cyan'))
        out = f'[identYwaf] [Waf!] {row.split("+] ")[1]}'
    elif '[=]' in row:
        print(gl.get('time')() + gl.get('+') + gl.get('col')('[identYwaf]', 'yellow') + ' ' + gl.get('col')(
            '[info]', 'yellow') + ' ' + gl.get('col')(
            row.split('=] ')[1], 'cyan'))
        out = f'[identYwaf] [info] {row.split("=] ")[1]}'
    output(out)


@lock_print
def TideFinger(row):
    out = ''
    if 'Banner:' in row:
        print(gl.get('time')() + gl.get('+') + gl.get('col')('[TideFinger]', 'yellow') + ' ' + gl.get('col')(
            '[Banner]', 'green') + ' ' + row.split('Banner:')[1])
        out = f"[TideFinger] [Banner] {row.split('Banner:')[1]}"
    elif 'CMS_finger:' in row:
        if 'Not Found' in row and gl.get('info'):
            print(gl.get('time')() + gl.get('*') + gl.get('col')('[TideFinger]', 'yellow') + ' ' + gl.get('col')(
                '[CMS]', 'green') + ' ' + row.split('CMS_finger:')[1])

        elif 'Not Found' not in row:
            print(gl.get('time')() + gl.get('+') + gl.get('col')('[TideFinger]', 'yellow') + ' ' + gl.get('col')(
                '[CMS]', 'green') + ' ' + row.split('CMS_finger:')[1])
            out = f"[TideFinger] [CMS] {row.split('CMS_finger:')[1]}"
    output(out)

@lock_print
def ksubdomain(row):
    for i in row:
        i = i.replace('\n','')
        print(gl.get('time')() + gl.get('+') + gl.get('col')('[ksubdomain]', 'yellow') + ' ' + gl.get('col')(
                '[domain]', 'green') + ' ' + gl.get('col')(i,'cyan'))
        output(f"[ksubdomain] [domain] {i}")
