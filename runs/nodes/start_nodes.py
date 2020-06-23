"""
时间：2020/6/15
作者：lurui
功能：部署nodes并启动kubelet、kube-proxy

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')

时间：2020/6/22
作者：lurui
修改：ansible批量操作转调用shell执行
"""

import os
# import subprocess
# import time


def start_nodes():

    basedir = os.path.abspath('.')
    start_nodes_path = basedir + '/deploy/nodes'

    package_path = basedir + '/deploy/packages'
    nodespath = basedir + '/ansible/hosts/nodes_hosts'
    cfg_path = basedir + '/deploy/nodes/cfg'

    yml_path = basedir + '/ansible/nodes/nodes.yaml'

    os.system('chmod +x {0}/start_nodes.sh'.format(start_nodes_path))

    os.system(start_nodes_path + '/start_nodes.sh ' + start_nodes_path + '' + nodespath + '' + package_path + '' + cfg_path + '' + yml_path)




    # print("Sir,Starting Copy Nodes Bin!")
    # try:
    #     copy_nodes_bin = subprocess.check_output('''ansible nodes -i {0} -m copy -a "src={1}/kubernetes/nodes dest=/tmp/"'''.format(nodespath, package_path), shell=True)
    #     print(copy_nodes_bin.decode())
    #     add_nodes_bin = subprocess.check_output('''ansible nodes -i {0} -m shell -a "cd /tmp/nodes && chmod +x * && cp * /kubernetes/kubernetes/bin/ && rm -rf /tmp/*"'''.format(nodespath), shell=True)
    #     print(add_nodes_bin.decode())
    # except Exception as e:
    #     print(e)
    # print("Sir,Copy Nodes Bin Has Completed!")

    # print("Sir,Starting Copy Nodes Config!")
    # try:
    #     copy_nodes_cfg = subprocess.check_output('''ansible nodes -i {0} -m copy -a "src={1} dest=/tmp/"'''.format(nodespath, cfg_path), shell=True)
    #     print(copy_nodes_cfg.decode())
    #     add_nodes_cfg = subprocess.check_output('''ansible nodes -i {0} -m shell -a "cd /tmp/cfg/ && cp bootstrap.kubeconfig kubelet.kubeconfig kube-proxy.kubeconfig /kubernetes/kubernetes/cfg/ && rm -rf /tmp/*"'''.format(nodespath), shell=True)
    #     print(add_nodes_cfg.decode())
    # except Exception as e:
    #     print(e)
    # print("Sir,Copy Nodes Config Has Completed!")

    # print("Sir,Update Nodes Config!")
    # try:
    #     update_nodes_cfg = subprocess.check_output('''ansible-playbook -i {0} {1}/ansible/nodes/nodes.yaml'''.format(nodespath, basedir), shell=True)
    #     print(update_nodes_cfg.decode())
    #     print("Sir,Update Nodes Config Completed!")
    # except Exception as e:
    #     print(e)

    # print("Sir,Starting Start Nodes!")
    # try:
    #     start_nodes = subprocess.check_output('''ansible nodes -i {0} -m shell -a "systemctl daemon-reload && systemctl enable kubelet && systemctl restart kubelet && systemctl enable kube-proxy && systemctl restart kube-proxy"'''.format(nodespath), shell=True)
    #     print(start_nodes.decode())
    # except Exception as e:
    #     print(e)
    # print("Sir,Start Nodes Has Completed!")
    #
    # time.sleep(10)


# start_nodes()
