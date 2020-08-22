"""
时间：2020/6/16
作者：lurui
功能：在master部署并启动haproxy

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
import subprocess
import time


def start_haproxy():
    basedir = os.path.abspath('.')
    haproxy_path = basedir + '/deploy/haproxy'
    masterpath = basedir + '/ansible/hosts/master_hosts'

    print("Sir,Starting Install Haproxy!")
    try:
        install_haproxy_svc = subprocess.check_output('''ansible master -i {0} -m shell -a "apt-get install haproxy -y && systemctl stop haproxy"'''.format(masterpath), shell=True)
        print(install_haproxy_svc.decode())
    except Exception as e:
        print(e)
    print("Sir,Starting Install Haproxy Has Completed!")

    print("Sir,Starting Copy Haproxy Config!")
    try:
        copy_haproxy_cfg = subprocess.check_output('''ansible master -i {0} -m copy -a "src={1}/cfg/haproxy.cfg dest=/etc/haproxy/"'''.format(masterpath, haproxy_path), shell=True)
        print(copy_haproxy_cfg.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Haproxy Config Has Completed!")

    time.sleep(5)

    print("Sir,Starting Start Haproxy!")
    try:
        start_haproxy = subprocess.check_output('''ansible master -i {0} -m shell -a "systemctl daemon-reload && systemctl enable haproxy && systemctl restart haproxy"'''.format(masterpath), shell=True)
        print(start_haproxy.decode())
    except Exception as e:
        print(e)
    print("Sir,Start Haproxy Has Completed!")


# start_haproxy()
