"""
时间：2020/7/1
作者：lurui
功能：k8s集群节点打标签
"""
import os
import configparser

basedir = os.path.abspath('.')


def start_label():
    config = configparser.ConfigParser()
    config.read(basedir + '/cfg/config.ini')
    k = config['LABEL']['Key']
    v = config['LABEL']['Value']

    os.system('''kubectl get nodes | grep k8s-node | awk '{print $1}' > nodes_tmp.txt''')
    nodes_name = basedir + '/nodes_tmp.txt'
    nodes = open(nodes_name, mode="r", encoding='utf-8')

    for i in nodes.readlines():
        a = i.strip('\n').split('-')
        try:
            os.system('''kubectl label node k8s-node-{0}-{1}-{2} {3}={4}{0}-{1}-{2}'''.format(a[1], a[2], a[3], k, v))
        except:
            os.system('''kubectl label node k8s-node-{0}-{1}-{2} {3}={4}{0}-{1}-{2} --overwrite'''.format(a[1], a[2], a[3], k, v))


start_label()
