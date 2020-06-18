"""
时间：2020/6/16
作者：lurui
功能：在master部署并启动keepalived

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
import subprocess
import time


def start_keepalived():
    basedir = os.path.abspath('.')
    keepalived_path = basedir + '/deploy/keepalived'
    masterpath = basedir + '/ansible/hosts/master_hosts'


    print("Sir,Starting Install Keepalived!")
    try:
        install_keepalived_svc = subprocess.check_output('''ansible master -i {0} -m shell -a "yum -y install keepalived && systemctl stop keepalived"'''.format(masterpath), shell=True)
        print(install_keepalived_svc.decode())
    except Exception as e:
        print(e)
    print("Sir,Starting Install Keepalived Has Completed!")


    print("Sir,Starting Copy Keepalived Config!")
    try:
        copy_keepalived_cfg = subprocess.check_output('''ansible-playbook -i {0} {1}/cfg/keepalived.yaml'''.format(masterpath, keepalived_path), shell=True)
        print(copy_keepalived_cfg.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Keepalived Config Has Completed!")

    print("Sir,Starting Copy Check_Haproxy Script!")
    try:
        copy_check_haproxy_script = subprocess.check_output('''ansible master -i {0} -m copy -a "src={1}/cfg/check_haproxy.sh dest=/etc/keepalived/"'''.format(masterpath, keepalived_path), shell=True)
        print(copy_check_haproxy_script.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Check_Haproxy Script Has Completed!")

    time.sleep(5)

    print("Sir,Starting Start Keepalived!")
    try:
        start_keepalived = subprocess.check_output('''ansible master -i {0} -m shell -a "systemctl daemon-reload && systemctl enable keepalived && systemctl restart keepalived"'''.format(masterpath), shell=True)
        print(start_keepalived.decode())
    except Exception as e:
        print(e)
    print("Sir,Start Keepalived Has Completed!")


# start_keepalived()
