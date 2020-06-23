"""
时间：2020/6/13
作者：lurui
功能：部署flanneld并启动flanneld+docker

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')

时间：2020/6/23
作者：lurui
修改：ansible批量操作转调用shell执行
"""

import os
import subprocess
import time


def start_flanneld():
    # package_path = basedir + '/deploy/packages'
    # nodepath = basedir + '/ansible/hosts/nodes_hosts'
    # flanneld_cfg = basedir + '/deploy/flanneld/cfg'
    basedir = os.path.abspath('.')
    start_flanneld_path = basedir + '/deploy/flanneld'
    cert_path = basedir + '/certs'
    package_path = basedir + '/deploy/packages'
    nodespath = basedir + '/ansible/hosts/nodes_hosts'
    cfg_path = basedir + '/deploy/flanneld/cfg'

    yml_path = basedir + '/ansible/nodes/nodes.yaml'

    os.system('chmod +x {0}/start_flanneld.sh'.format(start_flanneld_path))

    os.system(start_flanneld_path + '/start_flanneld.sh ' + start_flanneld_path + ' ' + nodespath + ' ' + cert_path + ' ' + package_path + ' ' + cfg_path + ' ' + yml_path)






    # print("Sir,Starting Copy Node Cert!")
    # try:
    #     copy_nodes_cert = subprocess.check_output(
    #         '''ansible nodes -i {0} -m copy -a "src={1}/etcd dest=/tmp/"'''.format(nodepath, cert_path), shell=True)
    #     print(copy_nodes_cert.decode())
    #     add_nodes_cert = subprocess.check_output(
    #         '''ansible nodes -i {0} -m shell -a "cd /tmp/etcd/ && cp ca*pem server*pem /kubernetes/etcd/ssl/ && rm -rf /tmp/*"'''.format(
    #             nodepath), shell=True)
    #     print(add_nodes_cert.decode())
    # except Exception as e:
    #     print(e)
    # print("Sir,Copy Node Cert Has Completed!")

    # print("Sir,Starting Copy Flanneld Config!")
    # try:
    #     copy_flanneld_cfg = subprocess.check_output(
    #         '''ansible nodes -i {0} -m copy -a "src={1}/flanneld dest=/kubernetes/kubernetes/cfg/"'''.format(nodepath,
    #                                                                                                          flanneld_cfg),
    #         shell=True)
    #     print(copy_flanneld_cfg.decode())
    # except Exception as e:
    #     print(e)
    # print("Sir,Copy Flanneld Config Has Completed!")

    # print("Sir,Starting Copy Docker daemon.json!")
    # try:
    #     result = subprocess.check_output('''ansible nodes -i {0} -m shell -a "mkdir -p /etc/docker"'''.format(nodepath),
    #                                      shell=True)
    #     print(result.decode())
    #     a = subprocess.check_output(
    #         '''ansible nodes -i {0} -m copy -a "src={1}/kubernetes/nodes/daemon.json dest=/etc/docker/"'''.format(
    #             nodepath, package_path), shell=True)
    #     print(a.decode())
    #     print("Sir,Copy Docker daemon.json Completed!")
    # except Exception as e:
    #     print(e)

    # print("Sir,Starting Copy Flanneld Bin!")
    # try:
    #     copy_flanneld_bin = subprocess.check_output(
    #         '''ansible nodes -i {0} -m copy -a "src={1}/flanneld dest=/tmp/"'''.format(nodepath, package_path),
    #         shell=True)
    #     print(copy_flanneld_bin.decode())
    #     add_flanneld_bin = subprocess.check_output(
    #         '''ansible nodes -i {0} -m shell -a "cd /tmp/flanneld && chmod +x * && cp * /kubernetes/kubernetes/bin/ && rm -rf /tmp/*"'''.format(
    #             nodepath), shell=True)
    #     print(add_flanneld_bin.decode())
    # except Exception as e:
    #     print(e)
    # print("Sir,Copy Flanneld Bin Has Completed!")

    # print("Sir,Starting Start Flanneld And Docker!")
    # try:
    #     try:
    #         start_flanneld = subprocess.check_output(
    #             '''ansible nodes -i {0} -m shell -a "systemctl daemon-reload && systemctl enable flanneld && systemctl restart flanneld"'''.format(
    #                 nodepath), shell=True)
    #         print(start_flanneld.decode())
    #     except Exception as e:
    #         print(e)
    #
    #     try:
    #         start_docker = subprocess.check_output(
    #             '''ansible nodes -i {0} -m shell -a "sysctl -p  /etc/sysctl.d/kubernetes.conf && systemctl restart docker && systemctl enable docker"'''.format(
    #                 nodepath), shell=True)
    #         print(start_docker.decode())
    #     except Exception as e:
    #         print(e)
    # except Exception as e:
    #     print(e)
    # print("Sir,Start Flanneld And Docker Has Completed!")


# start_flanneld()
