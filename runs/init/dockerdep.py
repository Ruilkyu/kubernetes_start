"""
时间：2020/6/13
作者：lurui
功能：初始化Docker环境,包括：
docker-compose安装
docker安装
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


def dockerdep():
    basedir = os.path.abspath('.')
    hostspath = basedir + '/ansible/hosts/nodes_hosts'
    dockerpath = basedir + '/deploy/init-env/docker-dep'

    start_init_path = basedir + '/deploy/init-env'

    os.system('chmod +x {0}/start_docker.sh'.format(start_init_path))

    os.system(start_init_path + '/start_docker.sh ' + start_init_path + ' ' + hostspath + ' ' + dockerpath)

    # print("Sir,Starting Copy docker-compose!")
    # try:
    #     copy_dockercompose = subprocess.check_output(
    #         '''ansible nodes -i {0} -m copy -a "src={1}/docker-compose dest=/usr/local/bin/"'''.format(
    #             hostspath, dockerpath), shell=True)
    #     print(copy_dockercompose.decode())
    #     give_x_dockercompose = subprocess.check_output(
    #         '''ansible nodes -i {0} -m shell -a "chmod +x /usr/local/bin/docker-compose"'''.format(
    #             hostspath), shell=True)
    #     print(give_x_dockercompose.decode())
    # except Exception as e:
    #     print(e)
    # print("Sir,Copy docker-compose Has Completed!")

    # print("Sir,Starting Add Docker!")
    # try:
    #     a = subprocess.check_output(
    #         '''ansible nodes -i {0} -m copy -a "src={1}/docker dest=/tmp/"'''.format(hostspath, dockerpath),
    #         shell=True)
    #     print(a.decode())
    #     b = subprocess.check_output(
    #         '''ansible nodes -i {0} -m shell -a "cd /tmp/docker/ && chmod +x * && mv * /usr/bin/"'''.format(hostspath), shell=True)
    #     print(b.decode())
    #     print("Sir,Add Docker Completed!")
    # except Exception as e:
    #     print(e)

    # print("Sir,Starting Add Config Files!")
    # try:
    #     a = subprocess.check_output(
    #         '''ansible nodes -i {0} -m copy -a "src={1}/docker.service dest=/usr/lib/systemd/system/docker.service"'''.format(
    #             hostspath, dockerpath), shell=True)
    #     print(a.decode())
    #     b = subprocess.check_output(
    #         '''ansible nodes -i {0} -m copy -a "src={1}/kubernetes.conf dest=/etc/sysctl.d/kubernetes.conf"'''.format(
    #             hostspath, dockerpath), shell=True)
    #     print(b.decode())
    #     c = subprocess.check_output(
    #         '''ansible nodes -i {0} -m copy -a "src={1}/flanneld.service dest=/usr/lib/systemd/system/flanneld.service"'''.format(
    #             hostspath, dockerpath), shell=True)
    #     print(c.decode())
    #     d = subprocess.check_output(
    #         '''ansible nodes -i {0} -m copy -a "src={1}/kubelet.service dest=/usr/lib/systemd/system/kubelet.service"'''.format(
    #             hostspath, dockerpath), shell=True)
    #     print(d.decode())
    #     e = subprocess.check_output(
    #         '''ansible nodes -i {0} -m copy -a "src={1}/kube-proxy.service dest=/usr/lib/systemd/system/kube-proxy.service"'''.format(
    #             hostspath, dockerpath), shell=True)
    #     print(e.decode())
    #     print("Sir,Add Config Files Completed!")
    # except Exception as e:
    #     print(e)


# dockerdep()
