"""
时间：2020/6/15
作者：lurui
功能：在master部署并启动keepalived
"""

import os
import subprocess
import time


def start_keepalived():
    basedir = os.path.dirname(os.path.dirname(os.getcwd()))
    keepalived_path = basedir + '/deploy/keepalived'
    masterpath = basedir + '/ansible/hosts/master_hosts'

    print("Sir,Starting Copy Keepalived Config!")
    try:
        copy_keepalived_cfg = subprocess.check_output(
            '''ansible-playbook -i {0} {1}/cfg/keepalived.yaml'''.format(masterpath,
                                                                         keepalived_path),
            shell=True)
        print(copy_keepalived_cfg.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Keepalived Config Has Completed!")

    print("Sir,Starting Copy Check_Haproxy Script!")
    try:
        copy_check_haproxy_script = subprocess.check_output(
            '''ansible master -i {0} -m copy -a "src={1}/cfg/check_haproxy.sh dest=/etc/keepalived/"'''.format(
                masterpath, keepalived_path), shell=True)
        print(copy_check_haproxy_script.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Check_Haproxy Script Has Completed!")

    print("Sir,Starting Copy Keepalived Svc!")
    try:
        copy_keepalived_svc = subprocess.check_output(
            '''ansible master -i {0} -m copy -a "src={1}/svc/keepalived.service dest=/usr/lib/systemd/system/"'''.format(
                masterpath, keepalived_path), shell=True)
        print(copy_keepalived_svc.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Keepalived Svc Has Completed!")

    print("Sir,Starting Copy Keepalived Bin!")
    try:
        copy_keepalived_bin = subprocess.check_output(
            '''ansible master -i {0} -m copy -a "src={1}/bin/keepalived dest=/usr/sbin/"'''.format(masterpath,
                                                                                                   keepalived_path),
            shell=True)
        print(copy_keepalived_bin.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Keepalived Bin Has Completed!")

    time.sleep(5)

    print("Sir,Starting Start Keepalived!")
    try:
        start_keepalived = subprocess.check_output(
            '''ansible master -i {0} -m shell -a "systemctl daemon-reload && systemctl enable keepalived && systemctl restart keepalived"'''.format(
                masterpath), shell=True)
        print(start_keepalived.decode())
    except Exception as e:
        print(e)
    print("Sir,Start Keepalived Has Completed!")


start_keepalived()
