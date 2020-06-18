"""
时间：2020/6/13
作者：lurui
功能：生成证书

时间：2020/6/17
作者：lurui
修改：
1、基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
2、从系统获取module变量，改为从行参中获取
"""

import os
import sys

# module = sys.argv[1]


def gencerts(module):
    basedir = os.path.abspath('.')
    certpath = basedir + '/certs/'
    # print(certpath + 'start.sh ' + certpath + ' ' + module)
    os.system(certpath + 'start.sh ' + certpath + ' ' + module)


# gencerts()
