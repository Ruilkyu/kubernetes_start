"""
时间：2020/6/12
作者：lurui
功能：根据提供的nodes模块列表生成nodes的ansible模块的nodes_hosts文件

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

    nodes_list = basedir + '/cfg/nodes.txt'
    try:
        nodes_list_fh = open(nodes_list, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(nodes_list)
        nodes_list_fh = open(nodes_list, mode="r", encoding='utf-8')

    if os.path.exists(basedir + '/ansible/hosts/nodes_hosts'):
        os.remove(basedir + '/ansible/hosts/nodes_hosts')

    if not os.path.exists(basedir + '/ansible/hosts'):
        os.makedirs(basedir + '/ansible/hosts')

    nodes_ansible_hosts_data = ''
    nodes_ansible_hosts_data = nodes_ansible_hosts_data + "[all:vars]" + "\n"
    nodes_ansible_hosts_data = nodes_ansible_hosts_data + "ansible_ssh_port={0}".format(port) + "\n" + "\n"
    nodes_ansible_hosts_data = nodes_ansible_hosts_data + "[nodes]" + "\n"
    try:
        for k in nodes_list_fh.readlines():
            result = k.strip("\n").split(".")
            first = result[2]
            second = result[3]
            v = k.strip("\n")
            nodes_ansible_hosts_data += v + " node_name=k8s-node-{0}-{1} ".format(first, second) + "node_ip={0}".format(
                v) + "\n"
    except Exception as e:
        print(e)

    try:
        location = basedir + '/ansible/hosts/nodes_hosts'
        file = open(location, 'a')

        resultdate = ""
        resultdate = nodes_ansible_hosts_data

        file.write(resultdate)
        file.close()
    except Exception as e:
        print(e)


# start_ansible_hosts()
