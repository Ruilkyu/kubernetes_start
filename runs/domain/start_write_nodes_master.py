"""
时间：2020/6/15
作者：lurui
功能：向master中写入nodes的对应关系(例如：10.10.52.30 k8s-node52-30)

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
import subprocess
import configparser


def start_write_nodes_master():
    basedir = os.path.abspath('.')
    listpath = basedir + '/cfg/nodes.txt'
    masterpath = basedir + '/ansible/hosts/master_hosts'

    try:
        ipfile = open(listpath, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(listpath)
        ipfile = open(listpath, mode="r", encoding='utf-8')

    print("BOSS,Starting Write Nodes Domain To Master!")
    try:
        for i in ipfile.readlines():
            i = i.strip()
            first = i.split('.')[0]
            second = i.split('.')[1]
            third = i.split('.')[2]
            fouth = i.split('.')[3]
            try:
                subprocess.check_output(
                    '''ansible master -i {0} -m shell -a "echo '{0}.{1}.{2}.{3} k8s-node-{2}-{3}' >> /etc/hosts"'''.format(masterpath, first, second, third, fouth), shell=True)
                print("BOSS,Write Nodes Domain To Master Completed!")
            except Exception as e:
                print(e)

    except Exception as e:
        print(e)


# start_write_nodes_master()
