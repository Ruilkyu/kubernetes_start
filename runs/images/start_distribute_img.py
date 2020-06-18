"""
时间：2020/6/15
作者：lurui
功能：分发基础pod镜像(registry.cn-hangzhou.aliyuncs.com/google-containers/pause-amd64:3.0)

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
import subprocess


def start_distribute_img():
    basedir = os.path.abspath('.')
    imgpath = basedir + '/deploy/packages/images'
    nodespath = basedir + '/ansible/hosts/nodes_hosts'

    print("Sir,Starting Distribute Pod Images!")
    try:
        distribute_pod_img = subprocess.check_output(
            '''ansible nodes -i {0} -m copy -a "src={1}/basepod.tar dest=/tmp/"'''.format(nodespath, imgpath),
            shell=True)
        print(distribute_pod_img.decode())
        add_pod_img = subprocess.check_output(
            '''ansible nodes -i {0} -m shell -a "cd /tmp/ && docker load < basepod.tar"'''.format(
                nodespath), shell=True)
        print(add_pod_img.decode())
    except Exception as e:
        print(e)
    print("Sir,Distribute Pod Images Has Completed!")


# start_distribute_img()
