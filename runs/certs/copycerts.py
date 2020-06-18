"""
时间：2020/6/16
作者：lurui
功能：拷贝Etcd证书(Master/Nodes)

时间：2020/6/17
作者：lurui
修改：
1、基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
2、从系统获取module变量，改为从行参中获取
"""

import os
import sys
import subprocess

# module = sys.argv[1]


def copycerts(module):
    basedir = os.path.abspath('.')
    certpath = basedir + '/certs/'

    hostspath = basedir + '/ansible/hosts'
    masterpath = hostspath + '/master_hosts'
    nodespath = hostspath + '/nodes_hosts'

    if module == "master":
        print("Sir,Starting Copy Master's Etcd Cert!")
        try:
            copy_master_etcd_cert = subprocess.check_output(
                '''ansible master -i {0} -m copy -a "src={1}/etcd dest=/tmp/"'''.format(masterpath, certpath),
                shell=True)
            print(copy_master_etcd_cert.decode())
            add_master_etcd_cert = subprocess.check_output(
                '''ansible master -i {0} -m shell -a "cd /tmp/etcd/ && cp ca*pem server*pem /kubernetes/etcd/ssl/ && 
                rm -rf /tmp/*"'''.format(
                    masterpath), shell=True)
            print(add_master_etcd_cert.decode())
        except Exception as e:
            print(e)
        print("Sir,Copy Master's Etcd Cert Has Completed!")

    if module == "nodes":
        print("Sir,Starting Copy Nodes's Etcd Cert!")
        try:
            copy_nodes_etcd_cert = subprocess.check_output(
                '''ansible nodes -i {0} -m copy -a "src={1}/etcd dest=/tmp/"'''.format(nodespath, certpath),
                shell=True)
            print(copy_nodes_etcd_cert.decode())
            add_nodes_etcd_cert = subprocess.check_output(
                '''ansible nodes -i {0} -m shell -a "cd /tmp/etcd/ && cp ca*pem server*pem /kubernetes/etcd/ssl/ && 
                rm -rf /tmp/*"'''.format(
                    nodespath), shell=True)
            print(add_nodes_etcd_cert.decode())
        except Exception as e:
            print(e)
        print("Sir,Copy Nodes's Etcd Cert Has Completed!")


# copycerts()
