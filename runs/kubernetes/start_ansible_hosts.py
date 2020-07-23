"""
时间：2020/6/12
作者：lurui
功能：根据提供的模块列表生成master的ansible模块的master_hosts文件

时间：2020/6/16
作者：lurui
修改：系统传参数方式改为读配置文件,读master.txt文件改为读config.ini

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')

时间：2020/7/23
作者：lurui
修改：调整支持1、3节点
"""

import os
import configparser


def start_ansible_hosts():
    basedir = os.path.abspath('.')
    config = configparser.ConfigParser()
    # config.read(basedir + '/cfg/ssh.ini')
    config.read(basedir + '/cfg/config.ini')
    port = config['SSH']['port']
    master_nums = int(config['MASTER']['nums'])

    # master_list = basedir + '/cfg/master.txt'
    # try:
    #     master_list_fh = open(master_list, mode="r", encoding='utf-8')
    # except FileNotFoundError:
    #     os.mknod(master_list)
    #     master_list_fh = open(master_list, mode="r", encoding='utf-8')

    master_ansible_hosts_templates = basedir + '/templates/kubernetes/ansible/hosts/{0}.yaml'.format(master_nums)
    try:
        master_ansible_hosts_templates_fh = open(master_ansible_hosts_templates, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(master_ansible_hosts_templates)
        master_ansible_hosts_templates_fh = open(master_ansible_hosts_templates, mode="r", encoding='utf-8')

    if os.path.exists(basedir + '/ansible/hosts/master_hosts'):
        os.remove(basedir + '/ansible/hosts/master_hosts')

    if not os.path.exists(basedir + '/ansible/hosts'):
        os.makedirs(basedir + '/ansible/hosts')

    master_ansible_hosts_data = ''
    try:
        for k in master_ansible_hosts_templates_fh.readlines():
            master_ansible_hosts_data += k
    except Exception as e:
        print(e)

    try:
        location = basedir + '/ansible/hosts/master_hosts'
        file = open(location, 'a')

        # masterlist = []
        #
        # for l in master_list_fh.readlines():
        #     masterlist.append(l.strip("\n"))

        resultdate = ""
        if master_nums == 1:
            master1 = config['MASTER']['master1']
            resultdate = master_ansible_hosts_data.format(master1, port)
        elif master_nums == 3:
            master1 = config['MASTER']['master1']
            master2 = config['MASTER']['master2']
            master3 = config['MASTER']['master3']
            resultdate = master_ansible_hosts_data.format(master1, master2, master3, port)

        # resultdate = ""
        # resultdate = master_ansible_hosts_data.format(master1, master2, master3, port)
        # resultdate = master_ansible_hosts_data.format(masterlist[0], masterlist[1], masterlist[2], port)

        file.write(resultdate)
        file.close()
    except Exception as e:
        print(e)


# start_ansible_hosts()
