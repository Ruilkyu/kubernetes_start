#!/bin/bash

cd ${1}

echo "BOSS,Starting Copy docker-compose!"

ansible nodes -i ${2} -m copy -a "src=${3}/docker-compose dest=/usr/local/bin/"
ansible nodes -i ${2} -m shell -a "chmod +x /usr/local/bin/docker-compose"

echo "BOSS,Copy docker-compose Has Completed!"

echo "BOSS,Starting Add Docker!"

ansible nodes -i ${2} -m copy -a "src=${3}/docker dest=/tmp/"
ansible nodes -i ${2} -m shell -a "cd /tmp/docker/ && chmod +x * && mv * /usr/bin/"

ansible nodes -i ${2} -m copy -a "src=${3}/gpu_docker dest=/tmp/ mode=777"
ansible nodes -i ${2} -m shell -a "cd /tmp/gpu_docker/nvidia-docker-bin/ && ./prepare.sh"
ansible nodes -i ${2} -m shell -a "cd /tmp/gpu_docker/nvidia-docker-dep/ && yes | dpkg -i *.deb"

echo "BOSS,Add Docker Completed!"

echo "BOSS,Starting Add Config Files!"

ansible nodes -i ${2} -m copy -a "src=${3}/gpu_docker/docker.service dest=/lib/systemd/system/docker.service"
ansible nodes -i ${2} -m copy -a "src=${3}/kubernetes.conf dest=/etc/sysctl.d/kubernetes.conf"
ansible nodes -i ${2} -m copy -a "src=${3}/flanneld.service dest=/lib/systemd/system/flanneld.service"
ansible nodes -i ${2} -m copy -a "src=${3}/kubelet.service dest=/lib/systemd/system/kubelet.service"
ansible nodes -i ${2} -m copy -a "src=${3}/kube-proxy.service dest=/lib/systemd/system/kube-proxy.service"

echo "BOSS,Add Config Files Completed!"