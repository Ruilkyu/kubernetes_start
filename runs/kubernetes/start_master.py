"""
时间：2020/6/13
作者：lurui
功能：部署master并启动kube-apiserver、kube-controller-manager、kube-scheduler-manager

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
import subprocess
import time


def start_master():
    basedir = os.path.abspath('.')
    cert_path = basedir + '/certs'
    package_path = basedir + '/deploy/packages'
    masterpath = basedir + '/ansible/hosts/master_hosts'
    cfg_path = basedir + '/deploy/master/cfg'

    print("Sir,Starting Copy Kube-Apiserver Config!")
    try:
        copy_api_svc = subprocess.check_output('''ansible master -i {0} -m copy -a "src={1}/api dest=/tmp/"'''.format(masterpath, cfg_path), shell=True)
        print(copy_api_svc.decode())
        add_api_svc = subprocess.check_output('''ansible master -i {0} -m shell -a "cd /tmp/api/ && cp kube-apiserver.service  /lib/systemd/system/kube-apiserver.service && cp token.csv /kubernetes/kubernetes/cfg/token.csv && rm -rf /tmp/*"'''.format(masterpath), shell=True)
        print(add_api_svc.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Kube-Apiserver Config Has Completed!")

    print("Sir,Starting Copy Kube-Controller-Manager Config!")
    try:
        copy_controller = subprocess.check_output('''ansible master -i {0} -m copy -a "src={1}/controller dest=/tmp/"'''.format(masterpath, cfg_path), shell=True)
        print(copy_controller.decode())
        add_controller = subprocess.check_output('''ansible master -i {0} -m shell -a "cd /tmp/controller/ && cp kube-controller-manager.service  /lib/systemd/system/kube-controller-manager.service && cp kube-controller-manager  /kubernetes/kubernetes/cfg/kube-controller-manager && rm -rf /tmp/*"'''.format(masterpath), shell=True)
        print(add_controller.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Kube-Controller-Manager Config Has Completed!")

    print("Sir,Starting Copy Kube-Scheduler Config!")
    try:
        copy_scheduler = subprocess.check_output('''ansible master -i {0} -m copy -a "src={1}/scheduler dest=/tmp/"'''.format(masterpath, cfg_path),
            shell=True)
        print(copy_scheduler.decode())
        add_scheduler = subprocess.check_output('''ansible master -i {0} -m shell -a "cd /tmp/scheduler/ && cp kube-scheduler.service  /lib/systemd/system/kube-scheduler.service && cp  kube-scheduler /kubernetes/kubernetes/cfg/kube-scheduler && rm -rf /tmp/*"'''.format(masterpath), shell=True)
        print(add_scheduler.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Kube-Scheduler Config Has Completed!")

    print("Sir,Starting Copy Master Cert!")
    try:
        copy_master_cert = subprocess.check_output('''ansible master -i {0} -m copy -a "src={1}/kubernetes dest=/tmp/"'''.format(masterpath, cert_path), shell=True)
        print(copy_master_cert.decode())
        add_master_cert = subprocess.check_output('''ansible master -i {0} -m shell -a "cd /tmp/kubernetes/ && cp *pem /kubernetes/kubernetes/ssl/ && rm -rf /tmp/*"'''.format(masterpath), shell=True)
        print(add_master_cert.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Master Cert Has Completed!")

    print("Sir,Starting Copy Master Bin!")
    try:
        copy_master_bin = subprocess.check_output('''ansible master -i {0} -m copy -a "src={1}/kubernetes/master dest=/tmp/"'''.format(masterpath, package_path), shell=True)
        print(copy_master_bin.decode())
    except Exception as e:
        print(e)
    try:
        add_master_bin = subprocess.check_output('''ansible master -i {0} -m shell -a "cd /tmp/master && chmod +x * && cp * /kubernetes/kubernetes/bin/ && rm -rf /tmp/*"'''.format(masterpath), shell=True)
        print(add_master_bin.decode())
    except Exception as e:
        print(e)
    print("Sir,Copy Master Bin Has Completed!")

    print("Sir,Update Kube-Apiserver Config!")
    try:
        update_api_svc = subprocess.check_output('''ansible-playbook -i {0} {1}/ansible/master/kube-apiserver.yaml'''.format(masterpath, basedir), shell=True)
        print(update_api_svc.decode())
        print("Sir,Update Kube-Apiserver Config Completed!")
    except Exception as e:
        print(e)

    print("Sir,Starting Start Master!")
    try:
        start_master = subprocess.check_output('''ansible master -i {0} -m shell -a "systemctl daemon-reload && systemctl enable kube-apiserver && systemctl restart kube-apiserver && systemctl enable kube-scheduler.service && systemctl restart kube-scheduler.service && systemctl enable kube-controller-manager && systemctl restart kube-controller-manager"'''.format(masterpath), shell=True)
        print(start_master.decode())
    except Exception as e:
        print(e)
    print("Sir,Start Master Has Completed!")

    time.sleep(10)

    print("Sir,Starting Access Controller!")
    try:
        start_access_control1 = subprocess.check_output('''ansible master -i {0} -m shell -a "/kubernetes/kubernetes/bin/kubectl create clusterrolebinding kubelet-bootstrap --clusterrole=system:node-bootstrapper --user=kubelet-bootstrap"'''.format(masterpath), shell=True)
        print(start_access_control1.decode())
    except Exception as e:
        print(e)
    try:
        start_access_control2 = subprocess.check_output('''ansible master -i {0} -m shell -a "/kubernetes/kubernetes/bin/kubectl create clusterrolebinding cluster-system-anonymous --clusterrole=cluster-admin --user=system:anonymous"'''.format(masterpath), shell=True)
        print(start_access_control2.decode())
    except Exception as e:
        print(e)
    print("Sir,Access Controller Has Completed!")


# start_master()
