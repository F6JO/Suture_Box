# -*- coding: utf-8 -*-
import os
import subprocess


# 执行命令并返回迭代器
def external_cmd(cmd, code):
  process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  while process.poll() is None:
    line = process.stdout.readline()
    line = line.strip()
    if line:
      yield line.decode(code, 'ignore')

# 执行命令并返回输出列表
def nuclei_cms(cmd):
    a = os.popen(cmd).readlines()
    return a

# 执行命令不反回
def dismap_cms(cmd):
    os.popen(cmd).read()



