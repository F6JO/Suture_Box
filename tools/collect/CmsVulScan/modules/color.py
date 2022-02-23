#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore, Back, Style, Cursor
init(autoreset=True)


class Colored:
    @staticmethod
    def magenta(s):
        # 紫色
        return Style.BRIGHT+Fore.MAGENTA+s+Fore.RESET+Style.RESET_ALL
    @staticmethod
    def green(s):
        # 绿色
        return Style.BRIGHT+Fore.GREEN+s+Fore.RESET+Style.RESET_ALL
    @staticmethod
    def white(s):
        # 白色
        return Fore.WHITE+s+Fore.RESET+Style.RESET_ALL
    @staticmethod
    def cyan(s):
        # 青色
        return Style.BRIGHT+Fore.CYAN+s+Fore.RESET+Style.RESET_ALL
    @staticmethod
    def cyan_fine(s):
        # 青色细
        return Fore.CYAN+s+Fore.RESET+Style.RESET_ALL
    @staticmethod
    def yellow(s):
        # 黄色
        return Style.BRIGHT+Fore.YELLOW+s+Fore.RESET+Style.RESET_ALL
    @staticmethod
    def red(s):
        # 红色
        return Style.BRIGHT+Fore.RED+s+Fore.RESET+Style.RESET_ALL
    @staticmethod
    def yel_info():
        # 黄色[INFO]
        return Style.BRIGHT+Fore.YELLOW+"[*]"+Fore.RESET+Style.RESET_ALL
    @staticmethod
    def red_warn():
        # 红色[WARN]
        return Style.BRIGHT+Fore.RED+"[-]"+Fore.RESET+Style.RESET_ALL
    @staticmethod
    def gre_ok():
        # 绿色[OK]
        return Style.BRIGHT+Fore.GREEN+"[+]"+Fore.RESET+Style.RESET_ALL


def Get_color():
    return Colored()
