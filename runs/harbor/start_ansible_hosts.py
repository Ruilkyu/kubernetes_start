"""
时间：2020/6/16
作者：lurui
功能：根据提供的模块列表生成harbor的ansible模块的harbor_hosts文件

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
import configparser


def start_ansible_hosts():
    basedir = os.path.abspath('.')
    config = configparser.ConfigParser()
    # config.read(basedir + '/cfg/ssh.ini')
    config.read(basedir + '/cfg/config.ini')
    port = config['SSH']['port']
    harbor_host = config['HARBOR']['host']

    harbor_ansible_hosts_templates = basedir + '/templates/harbor/ansible/hosts/hosts.yaml'
    try:
        harbor_ansible_hosts_templates_fh = open(harbor_ansible_hosts_templates, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(harbor_ansible_hosts_templates)
        harbor_ansible_hosts_templates_fh = open(harbor_ansible_hosts_templates, mode="r", encoding='utf-8')

    if os.path.exists(basedir + '/ansible/hosts/harbor_hosts'):
        os.remove(basedir + '/ansible/hosts/harbor_hosts')

    if not os.path.exists(basedir + '/ansible/hosts'):
        os.makedirs(basedir + '/ansible/hosts')

    harbor_ansible_hosts_data = ''
    try:
        for k in harbor_ansible_hosts_templates_fh.readlines():
            harbor_ansible_hosts_data += k
    except Exception as e:
        print(e)

    try:
        location = basedir + '/ansible/hosts/harbor_hosts'
        file = open(location, 'a')

        resultdate = ""
        resultdate = harbor_ansible_hosts_data.format(harbor_host, port)

        file.write(resultdate)
        file.close()
    except Exception as e:
        print(e)

# start_ansible_hosts()
