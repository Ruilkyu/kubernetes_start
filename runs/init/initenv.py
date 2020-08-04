"""
时间：2020/6/13
作者：lurui
功能：初始化环境,使用时传递module参数（master/etcd/nodes/harbor）

时间：2020/6/17
作者：lurui
修改：
1、基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
2、从系统获取module变量，改为从行参中获取

时间：2020/6/18
作者：lurui
修改：
1、兼容同一节点，多个服务（master/etcd nodes/etcd）

时间：2020/6/23
作者：lurui
修改：nodes模块的ansible批量操作转调用shell执行
"""

import os
import sys
import subprocess


# module = sys.argv[1]


def initenv(module):
    basedir = os.path.abspath('.')
    initpath = basedir + '/deploy/init-env/'
    hostspath = basedir + '/ansible/hosts'
    masterpath = hostspath + '/master_hosts'
    nodespath = hostspath + '/nodes_hosts'
    etcdpath = hostspath + '/etcd_hosts'
    harborpath = hostspath + '/harbor_hosts'

    dockerpath = basedir + '/deploy/init-env/docker-dep'
    docker_daemon_path = basedir + '/deploy/packages'

    start_init_path = basedir + '/deploy/init-env'

    os.system('chmod +x {0}/start_initenv.sh'.format(start_init_path))

    if module == "master":
        print("Sir,Starting Stop Old Kubernetes!")
        try:
            stop_kubernetes = subprocess.check_output(
                '''ansible master -i {0} -m shell -a "systemctl stop kube-apiserver && systemctl stop kube-controller-manager && systemctl stop kube-scheduler && systemctl stop kubelet && systemctl stop kube-proxy && systemctl stop flanneld && systemctl stop docker && rm -rf /var/lib/docker/*"'''.format(
                    masterpath), shell=True)
            print(stop_kubernetes.decode())
        except Exception as e:
            print(e)
        print("Sir,Old Kubernetes Has Stop!")

        print("Sir,Starting Delete Old Kubernetes!")
        try:
            delete_kubernetes = subprocess.check_output(
                '''ansible master -i {0} -m shell -a "rm -rf /kubernetes/kubernetes/*"'''.format(masterpath),
                shell=True)
            print(delete_kubernetes.decode())
        except Exception as e:
            print(e)
        print("Sir,Old Kubernetes Has Deleted!")

    if module == "nodes":
        os.system(start_init_path + '/start_initenv.sh ' + start_init_path + ' ' + nodespath)
        # print("Sir,Starting Stop Old Kubernetes!")
        # try:
        #     stop_kubernetes = subprocess.check_output(
        #         '''ansible nodes -i {0} -m shell -a "systemctl stop kubelet && systemctl stop kube-proxy && systemctl stop flanneld && systemctl stop docker && rm -rf /var/lib/docker/*"'''.format(
        #             nodespath), shell=True)
        #     print(stop_kubernetes.decode())
        # except Exception as e:
        #     print(e)
        # print("Sir,Old Kubernetes Has Stop!")
        #
        # print("Sir,Starting Delete Old Kubernetes!")
        # try:
        #     delete_kubernetes = subprocess.check_output(
        #         '''ansible nodes -i {0} -m shell -a "rm -rf /kubernetes/kubernetes/*"'''.format(nodespath),
        #         shell=True)
        #     print(delete_kubernetes.decode())
        # except Exception as e:
        #     print(e)
        # print("Sir,Old Kubernetes Has Deleted!")

    if module == "etcd":
        print("Sir,Starting Stop Old Etcd!")
        try:
            stop_etcd = subprocess.check_output(
                '''ansible etcd -i {0} -m shell -a "systemctl stop etcd && rm -rf /var/lib/etcd/*"'''.format(
                    etcdpath), shell=True)
            print(stop_etcd.decode())
        except Exception as e:
            print(e)
        print("Sir,Old Etcd Has Stop!")

        print("Sir,Starting Delete Old Etcd!")
        try:
            delete_etcd = subprocess.check_output(
                '''ansible etcd -i {0} -m shell -a "rm -rf /kubernetes/etcd/*"'''.format(etcdpath),
                shell=True)
            print(delete_etcd.decode())
        except Exception as e:
            print(e)
        print("Sir,Old Etcd Has Deleted!")

        print("Sir,Starting Add Etcd Config Files! ")
        try:
            copy_etcd_cfg = subprocess.check_output(
                '''ansible etcd -i {0} -m copy -a "src={1}/etcd.service dest=/usr/lib/systemd/system/etcd.service"'''.format(
                    etcdpath, dockerpath),
                shell=True)
            print(copy_etcd_cfg.decode())
        except Exception as e:
            print(e)
        print("Sir,Etcd Config Add Completed!")

    if module == "harbor":
        print("Sir,Starting Init Harbor Env!")
        os.system(initpath + 'start.sh ' + initpath + ' ' + hostspath + ' ' + module)
        print("Sir,Init Harbor Env Completed!")

        print("Sir,Starting Copy docker-compose!")
        try:
            copy_dockercompose = subprocess.check_output(
                '''ansible harbor -i {0} -m copy -a "src={1}/docker-compose dest=/usr/local/bin/"'''.format(
                    harborpath, dockerpath), shell=True)
            print(copy_dockercompose.decode())
            give_x_dockercompose = subprocess.check_output(
                '''ansible harbor -i {0} -m shell -a "chmod +x /usr/local/bin/docker-compose"'''.format(
                    harborpath), shell=True)
            print(give_x_dockercompose.decode())
        except Exception as e:
            print(e)
        print("Sir,Copy docker-compose Has Completed!")

        print("Sir,Starting Add Docker!")
        try:
            a = subprocess.check_output(
                '''ansible harbor -i {0} -m copy -a "src={1}/docker dest=/tmp/"'''.format(harborpath, dockerpath),
                shell=True)
            print(a.decode())
            b = subprocess.check_output(
                '''ansible harbor -i {0} -m shell -a "cd /tmp/docker/ && chmod +x * && mv * /usr/bin/"'''.format(
                    harborpath), shell=True)
            print(b.decode())
            print("Sir,Add Docker Completed!")
        except Exception as e:
            print(e)

        print("Sir,Starting Add Config Files!")
        try:
            a = subprocess.check_output(
                '''ansible harbor -i {0} -m copy -a "src={1}/harbor.service dest=/usr/lib/systemd/system/docker.service"'''.format(
                    harborpath, dockerpath), shell=True)
            print(a.decode())
            print("Sir,Add Config Files Completed!")
        except Exception as e:
            print(e)

        print("Sir,Starting Add daemon.json File!")
        try:
            a = subprocess.check_output(
                '''ansible harbor -i {0} -m copy -a "src={1}/kubernetes/nodes/daemon.json dest=/etc/docker/"'''.format(
                    harborpath, docker_daemon_path), shell=True)
            print(a.decode())
            print("Sir,Add daemon.json File Completed!")
        except Exception as e:
            print(e)

        print("Sir,Starting Run Docker!")
        try:
            a = subprocess.check_output(
                '''ansible harbor -i {0} -m shell -a "systemctl daemon-reload && systemctl enable docker && systemctl restart docker"'''.format(
                    harborpath), shell=True)
            print(a.decode())
            print("Sir,Run Docker Completed!")
        except Exception as e:
            print(e)

        print("Sir,Starting Stop Old Harbor!")
        try:
            stop_harbor = subprocess.check_output(
                '''ansible harbor -i {0} -m shell -a "cd /srv/harbor && docker-compose down && cd /srv && rm -rf harbor"'''.format(
                    harborpath), shell=True)
            print(stop_harbor.decode())
        except Exception as e:
            print(e)
        print("Sir,Old Harbor Has Stop!")

        print("Sir,Starting Copy New Harbor!")
        try:
            copy_new_harbor = subprocess.check_output(
                '''ansible harbor -i {0} -m copy -a "src={1}/deploy/packages/harbor dest=/srv/"'''.format(harborpath,
                                                                                                          basedir),
                shell=True)
            print(copy_new_harbor.decode())
        except Exception as e:
            print(e)
        print("Sir,Copy New Harbor Has Completed!")

    os.system(initpath + 'start.sh ' + initpath + ' ' + hostspath + ' ' + module)

# initenv()
