"""
时间：2020/9/22
作者：lurui
功能：k8s集群GPU节点打标签
"""
import os
import sys

basedir = os.path.abspath('.')


def start_label_gpu(k, v):
    nodes_name = basedir + '/cfg/nodes.txt'
    nodes = open(nodes_name, mode="r", encoding='utf-8')

    for i in nodes.readlines():
        a = i.strip('\n').split('.')
        try:
            os.system('''kubectl label node k8s-node-{0}-{1}-{2} {3}={4}'''.format(a[1], a[2], a[3], k, v))
        except Exception as e:
            print(e)
            os.system('''kubectl label node k8s-node-{0}-{1}-{2} {3}={4} --overwrite'''.format(a[2], a[3], a[4], k, v))


a = sys.argv[1]
b = sys.argv[2]
start_label_gpu(a, b)
