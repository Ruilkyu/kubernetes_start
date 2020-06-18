"""
时间：2020/6/13
作者：lurui
功能：根据提供的模版，生成haprocy对应的haproxy.cfg配置文件

时间：2020/6/16
作者：lurui
修改：读master.txt文件改为读config.ini

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
import configparser


def start_haproxy_cfg():
    basedir = os.path.abspath('.')
    config = configparser.ConfigParser()
    # config.read(basedir + '/cfg/vip.ini')
    config.read(basedir + '/cfg/config.ini')
    vip = config['VIP']['vip']
    port = config['VIP']['port']

    # master_list = basedir + '/cfg/master.txt'
    # try:
    #     master_list_fh = open(master_list, mode="r", encoding='utf-8')
    # except FileNotFoundError:
    #     os.mknod(master_list)
    #     master_list_fh = open(master_list, mode="r", encoding='utf-8')

    haproxy_templates = basedir + '/templates/haproxy/haproxy.yaml'
    try:
        haproxy_templates_fh = open(haproxy_templates, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(haproxy_templates)
        haproxy_templates_fh = open(haproxy_templates, mode="r", encoding='utf-8')

    if os.path.exists(basedir + '/deploy/haproxy/cfg/haproxy.cfg'):
        os.remove(basedir + '/deploy/haproxy/cfg/haproxy.cfg')

    if not os.path.exists(basedir + '/deploy/haproxy/cfg'):
        os.makedirs(basedir + '/deploy/haproxy/cfg')

    haproxy_data = ''
    try:
        for k in haproxy_templates_fh.readlines():
            haproxy_data += k
    except Exception as e:
        print(e)

    try:
        location = basedir + '/deploy/haproxy/cfg/haproxy.cfg'
        file = open(location, 'a')

        # masterlist = []
        #
        # for l in master_list_fh.readlines():
        #     masterlist.append(l.strip("\n"))

        master1 = config['MASTER']['master1']
        master2 = config['MASTER']['master2']
        master3 = config['MASTER']['master3']

        resultdate = ""
        resultdate = haproxy_data.format(port, master1, master2, master3)

        file.write(resultdate)
        file.close()
    except Exception as e:
        print(e)


# start_haproxy_cfg()
