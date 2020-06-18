"""
时间：2020/6/15
作者：lurui
功能：生成nodes的认证配置文件

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os


def gennodescfg():
    basedir = os.path.abspath('.')
    cfgpath = basedir + '/deploy/nodes/cfg'

    os.system('chmod +x {0}/genconfig.sh'.format(cfgpath))

    os.system(cfgpath + '/genconfig.sh ' + cfgpath)


# gennodescfg()
