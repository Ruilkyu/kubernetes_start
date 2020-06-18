"""
时间：2020/6/13
作者：lurui
功能：部署etcd

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
import sys
import subprocess
import time


def start_etcd():
    basedir = os.path.abspath('.')
    cert_path = basedir + '/certs'
    package_path = basedir + '/deploy/packages'
    etcdpath = basedir + '/ansible/hosts/etcd_hosts'
    networkpath = basedir + '/deploy/etcd'


    print("Sir,Starting Copy Etcd Cert!")
    try:
        copy_etcd_cert = subprocess.check_output('''ansible etcd -i {0} -m copy -a "src={1}/etcd dest=/tmp/"'''.format(etcdpath, cert_path), shell=True)
        print(copy_etcd_cert.decode())
        add_etcd_cert = subprocess.check_output('''ansible etcd -i {0} -m shell -a "cd /tmp/etcd/ && cp ca*pem server*pem /kubernetes/etcd/ssl/ && rm -rf /tmp/*"'''.format(etcdpath), shell=True)
        print(add_etcd_cert.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Etcd Cert Has Completed!")

    print("Sir,Starting Copy Etcd Bin!")
    try:
        copy_etcd_bin = subprocess.check_output('''ansible etcd -i {0} -m copy -a "src={1}/etcd dest=/tmp/"'''.format(etcdpath, package_path), shell=True)
        print(copy_etcd_bin.decode())
        add_etcd_bin = subprocess.check_output('''ansible etcd -i {0} -m shell -a "cd /tmp/etcd && chmod +x * && cp * /kubernetes/etcd/bin/ && rm -rf /tmp/*"'''.format(etcdpath), shell=True)
        print(add_etcd_bin.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Etcd Bin Has Completed!")

    print("Sir,Update Etcd Config!")
    try:
        update_etcd = subprocess.check_output('''ansible-playbook -i {0} {1}/ansible/etcd/etcd.yaml'''.format(etcdpath, basedir), shell=True)
        print(update_etcd.decode())
        print("Sir,Update Etcd Completed!")
    except Exception as e:
        print(e)


    print("Sir,Starting Start Etcd!")
    try:
        start_etcd = subprocess.check_output('''ansible etcd -i {0} -m shell -a "systemctl daemon-reload && systemctl enable etcd && systemctl start etcd"'''.format(etcdpath), shell=True)
        print(start_etcd.decode())
    except Exception as e:
        print(e)
    print("Sir,Start Etcd Has Completed!")

    time.sleep(10)

    print("Sir,Starting Write Etcd Network!")
    try:
        copy_etcd_network = subprocess.check_output('''ansible etcd -i {0} -m copy -a "src={1}/network.sh dest=/tmp/"'''.format(etcdpath, networkpath), shell=True)
        print(copy_etcd_network.decode())
        write_etcd_network = subprocess.check_output('''ansible etcd -i {0} -m shell -a "cd /tmp/ && chmod +x network.sh && ./network.sh"'''.format(etcdpath), shell=True)
        print(write_etcd_network.decode())
    except Exception as e:
        print(e)
    print("Sir,Write Etcd Network Completed!")


# start_etcd()
