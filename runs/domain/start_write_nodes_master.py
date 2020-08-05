"""
时间：2020/6/15
作者：lurui
功能：向master中写入nodes的对应关系(例如：10.10.52.30 k8s-node52-30)
时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
时间：2020/8/4
作者：lurui
修改：修改/etc/hosts写入IP
时间：2020/8/4
作者：lurui
修改：for循环改为multiprocessing.Pool.map方法（并行化）
"""

import os
import subprocess
import configparser
from multiprocessing import Pool


def write_nodes_domain(ip_str):
    basedir = os.path.abspath('.')
    masterpath = basedir + '/ansible/hosts/master_hosts'
    i = str(ip_str).strip()
    first = i.split('.')[0]
    second = i.split('.')[1]
    third = i.split('.')[2]
    fouth = i.split('.')[3]
    try:
        # subprocess.check_output(
        #     '''ansible master -i {0} -m shell -a "echo '{1}.{2}.{3}.{4} k8s-node-{3}-{4}' >> /etc/hosts"'''.format(
        #         masterpath, first, second, third, fouth), shell=True)
        tmp = subprocess.check_output(
            '''ansible master -i {0} -m shell -a "cat /etc/hosts | grep {1}.{2}.{3}.{4}"'''.format(
                masterpath, first, second, third, fouth), shell=True)
    except subprocess.CalledProcessError:
        subprocess.check_output(
            '''ansible master -i {0} -m shell -a "echo '{1}.{2}.{3}.{4} k8s-node-{3}-{4}' >> /etc/hosts"'''.format(
                masterpath, first, second, third, fouth), shell=True)
    except Exception as e:
        print(e)


def start_write_nodes_master():
    basedir = os.path.abspath('.')
    listpath = basedir + '/cfg/nodes.txt'
    masterpath = basedir + '/ansible/hosts/master_hosts'

    ip_list = []

    try:
        ipfile = open(listpath, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(listpath)
        ipfile = open(listpath, mode="r", encoding='utf-8')

    print("BOSS,Starting Write Nodes Domain To Master!")
    try:
        for i in ipfile.readlines():
            i = i.strip()
            ip_list.append(i)
            # first = i.split('.')[0]
            # second = i.split('.')[1]
            # third = i.split('.')[2]
            # fouth = i.split('.')[3]
            # try:
            #     subprocess.check_output(
            #         '''ansible master -i {0} -m shell -a "echo '{0}.{1}.{2}.{3} k8s-node-{2}-{3}' >> /etc/hosts"'''.format(
            #             masterpath, first, second, third, fouth), shell=True)
            #     print("BOSS,Write Nodes Domain To Master Completed!")
            # except Exception as e:
            #     print(e)

    except Exception as e:
        print(e)
    try:
        pool = Pool()
        pool.map(write_nodes_domain, ip_list)
        pool.close()
        pool.join()
    except Exception as e:
        print(e)
    print("BOSS,Write Nodes Domain To Master Completed!")




# start_write_nodes_master()