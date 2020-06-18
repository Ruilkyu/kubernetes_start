"""
时间：2020/6/12
作者：lurui
功能：根据提供的模块列表生成kubernetes对应的server-csr.json文件

时间：2020/6/16
作者：lurui
修改：读master.txt文件改为读config.ini

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
import configparser


def start_cert():
    basedir = os.path.abspath('.')
    config = configparser.ConfigParser()
    config.read(basedir + '/cfg/config.ini')
    # master_list = basedir + '/cfg/master.txt'
    # try:
    #     master_list_fh = open(master_list, mode="r", encoding='utf-8')
    # except FileNotFoundError:
    #     os.mknod(master_list)
    #     master_list_fh = open(master_list, mode="r", encoding='utf-8')

    master_cert_templates = basedir + '/templates/kubernetes/certs/3.yaml'
    try:
        master_cert_templates_fh = open(master_cert_templates, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(master_cert_templates)
        master_cert_templates_fh = open(master_cert_templates, mode="r", encoding='utf-8')

    if os.path.exists(basedir + '/certs/kubernetes/server-csr.json'):
        os.remove(basedir + '/certs/kubernetes/server-csr.json')

    if not os.path.exists(basedir + '/certs/kubernetes'):
        os.makedirs(basedir + '/certs/kubernetes')

    master_cert_data = ''
    try:
        for k in master_cert_templates_fh.readlines():
            master_cert_data += k
    except Exception as e:
        print(e)

    try:
        location = basedir + '/certs/kubernetes/server-csr.json'
        file = open(location, 'a')

        # masterlist = []
        #
        # for l in master_list_fh.readlines():
        #     masterlist.append(l.strip("\n"))

        master1 = config['MASTER']['master1']
        master2 = config['MASTER']['master2']
        master3 = config['MASTER']['master3']
        vip = config['VIP']['vip']

        resultdate = ""
        resultdate = master_cert_data.format(master1, master2, master3, vip)

        file.write(resultdate)
        file.close()
    except Exception as e:
        print(e)


# start_cert()
