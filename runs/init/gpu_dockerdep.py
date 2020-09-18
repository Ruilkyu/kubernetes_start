"""
时间：2020/9/18
作者：lurui
功能：初始化Docker环境,包括：
docker-compose安装
nvidia-docker安装
docker.service就位
flanneld.service就位
kube-proxy.service就位
kubelet.service就位
kubernetes.conf就位

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')

时间：2020/6/23
作者：lurui
修改：ansible批量操作转调用shell执行
"""

import os
import subprocess


def gpudockerdep():
    basedir = os.path.abspath('.')
    hostspath = basedir + '/ansible/hosts/nodes_hosts'
    dockerpath = basedir + '/deploy/init-env/docker-dep'

    start_init_path = basedir + '/deploy/init-env'

    os.system('chmod +x {0}/start_gpu_docker.sh'.format(start_init_path))

    os.system(start_init_path + '/start_gpu_docker.sh ' + start_init_path + ' ' + hostspath + ' ' + dockerpath)