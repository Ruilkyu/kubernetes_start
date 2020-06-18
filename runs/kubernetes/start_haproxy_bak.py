"""
时间：2020/6/13
作者：lurui
功能：在master部署并启动haproxy
"""

import os
import subprocess
import time


def start_haproxy():
    basedir = os.path.dirname(os.path.dirname(os.getcwd()))
    haproxy_path = basedir + '/deploy/haproxy'
    masterpath = basedir + '/ansible/hosts/master_hosts'

    print("Sir,Starting Copy Haproxy Config!")
    try:
        copy_haproxy_cfg = subprocess.check_output('''ansible master -i {0} -m copy -a "src={1}/cfg/haproxy.cfg dest=/etc/haproxy/"'''.format(masterpath, haproxy_path), shell=True)
        print(copy_haproxy_cfg.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Haproxy Config Has Completed!")

    print("Sir,Starting Copy Haproxy Svc!")
    try:
        copy_haproxy_svc = subprocess.check_output(
            '''ansible master -i {0} -m copy -a "src={1}/svc/haproxy.service dest=/usr/lib/systemd/system/"'''.format(masterpath, haproxy_path), shell=True)
        print(copy_haproxy_svc.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Haproxy Svc Has Completed!")

    print("Sir,Starting Copy Haproxy Bin!")
    try:
        copy_haproxy_bin = subprocess.check_output(
            '''ansible master -i {0} -m copy -a "src={1}/bin dest=/tmp/"'''.format(masterpath, haproxy_path), shell=True)
        print(copy_haproxy_bin.decode())
        add_haproxy_bin = subprocess.check_output('''ansible master -i {0} -m shell -a "systemctl stop haproxy && cd /tmp/bin && chmod +x * && cp * /usr/sbin/ && rm -rf /tmp/*"'''.format(masterpath), shell=True)
        print(add_haproxy_bin.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Haproxy Bin Has Completed!")

    time.sleep(5)

    print("Sir,Starting Start Haproxy!")
    try:
        start_haproxy = subprocess.check_output('''ansible master -i {0} -m shell -a "systemctl daemon-reload && systemctl enable haproxy && systemctl restart haproxy"'''.format(masterpath), shell=True)
        print(start_haproxy.decode())
    except Exception as e:
        print(e)
    print("Sir,Start Haproxy Has Completed!")


start_haproxy()
