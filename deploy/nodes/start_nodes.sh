#!/bin/bash

cd ${1}

echo "BOSS,Starting Copy Nodes Bin!"

ansible nodes -i ${2} -m copy -a "src=${3}/kubernetes/nodes dest=/tmp/"
ansible nodes -i ${2} -m shell -a "cd /tmp/nodes && chmod +x * && cp * /kubernetes/kubernetes/bin/ && rm -rf /tmp/*"

echo "BOSS,Copy Nodes Bin Has Completed!"


echo "BOSS,Starting Copy Nodes Config!"

ansible nodes -i ${2} -m copy -a "src=${4} dest=/tmp/"
ansible nodes -i ${2} -m shell -a "cd /tmp/cfg/ && cp bootstrap.kubeconfig kubelet.kubeconfig kube-proxy.kubeconfig /kubernetes/kubernetes/cfg/ && rm -rf /tmp/*"

echo "BOSS,Copy Nodes Config Has Completed!"

echo "BOSS,Update Nodes Config!"

ansible-playbook -i ${2} ${5}

echo "BOSS,Update Nodes Config Completed!"

echo "BOSS,Starting Start Nodes!"

ansible nodes -i ${2} -m shell -a "systemctl daemon-reload && systemctl enable kubelet && systemctl restart kubelet && systemctl enable kube-proxy && systemctl restart kube-proxy"

echo "BOSS,Start Nodes Has Completed!"