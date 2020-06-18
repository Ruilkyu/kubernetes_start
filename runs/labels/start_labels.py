"""
时间：2020/6/15
作者：lurui
功能：向master中标记nodes的labels(例如：k8s-node52-30 lotus=node5230)

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')

时间：2020/6/18
作者：lurui
修改：修改label占位符位置顺序
"""

import os
import subprocess


def start_labels_nodes():
    basedir = os.path.abspath('.')
    listpath = basedir + '/cfg/nodes.txt'
    masterpath = basedir + '/ansible/hosts/master_hosts'

    try:
        ipfile = open(listpath, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(listpath)
        ipfile = open(listpath, mode="r", encoding='utf-8')

    print("Sir,Starting Create Lotus Namespace!")
    try:
        subprocess.check_output('''ansible master -i {0} -m shell -a "/kubernetes/kubernetes/bin/kubectl create namespace lotus"'''.format(masterpath), shell=True)
        print("Sir,Create Lotus Namespace Completed!")
    except Exception as e:
        print(e)

    print("Sir,Starting Label Nodes!")
    try:
        for i in ipfile.readlines():
            i = i.strip()
            first = i.split('.')[2]
            second = i.split('.')[3]

            try:
                subprocess.check_output('''ansible master -i {0} -m shell -a "/kubernetes/kubernetes/bin/kubectl label nodes k8s-node-{1}-{2} lotus=node{1}{2}"'''.format(masterpath, first, second), shell=True)
                print("Sir,Label Nodes Completed!")
            except Exception as e:
                print(e)
                continue

    except Exception as e:
        print(e)


# start_labels_nodes()
