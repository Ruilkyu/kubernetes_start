#!/bin/bash

cd ${1}

echo "BOSS,Starting Copy Node Cert!"


ansible nodes -i ${2} -m copy -a "src=${3}/etcd dest=/tmp/"

ansible nodes -i ${2} -m shell -a "cd /tmp/etcd/ && cp ca*pem server*pem /kubernetes/etcd/ssl/ && rm -rf /tmp/*"


echo "BOSS,Copy Node Cert Has Completed!"


echo "BOSS,Starting Copy Flanneld Config!"

ansible nodes -i ${2} -m copy -a "src=${5}/flanneld dest=/kubernetes/kubernetes/cfg/"

echo "BOSS,Copy Flanneld Config Has Completed!"

echo "BOSS,Starting Copy Docker daemon.json!"

ansible nodes -i ${2} -m shell -a "mkdir -p /etc/docker"
ansible nodes -i ${2} -m copy -a "src=${4}/kubernetes/nodes/daemon.json dest=/etc/docker/"

echo "BOSS,Copy Docker daemon.json Completed!"


echo "BOSS,Starting Copy Flanneld Bin!"

ansible nodes -i ${2} -m copy -a "src=${4}/flanneld dest=/tmp/"
ansible nodes -i ${2} -m shell -a "cd /tmp/flanneld && chmod +x * && cp * /kubernetes/kubernetes/bin/ && rm -rf /tmp/*"

echo "BOSS,Copy Flanneld Bin Has Completed!"


echo "BOSS,Starting Start Flanneld And Docker!"

ansible nodes -i ${2} -m shell -a "systemctl daemon-reload && systemctl enable flanneld && systemctl restart flanneld"
ansible nodes -i ${2} -m shell -a "sysctl -p  /etc/sysctl.d/kubernetes.conf && systemctl restart docker && systemctl enable docker"

echo "BOSS,Start Flanneld And Docker Has Completed!"