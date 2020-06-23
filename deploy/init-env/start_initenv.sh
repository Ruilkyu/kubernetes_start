#!/bin/bash

cd ${1}


echo "BOSS,Starting Stop Old Kubernetes!"

ansible nodes -i ${2} -m shell -a "systemctl stop kubelet && systemctl stop kube-proxy && systemctl stop flanneld && systemctl stop docker && rm -rf /var/lib/docker/*"

echo "BOSS,Old Kubernetes Has Stop!"

echo "BOSS,Starting Delete Old Kubernetes!"

ansible nodes -i ${2} -m shell -a "rm -rf /kubernetes/kubernetes/*"

echo "BOSS,Old Kubernetes Has Deleted!"



