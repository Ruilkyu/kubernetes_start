#!/bin/bash
if [ "${2}" == "master" ];then
  ansible master -i ${1}/master_hosts -m shell -a "mkdir -p /var/log/kube-apiserver && mkdir -p /var/log/kube-controller-manager && mkdir -p /var/log/kube-scheduler && touch /var/log/kube-apiserver/kube-apiserver-audit.log && mkdir -p /kubernetes/etcd/bin && mkdir -p /kubernetes/etcd/cfg && mkdir -p /kubernetes/etcd/ssl && mkdir -p /kubernetes/kubernetes/bin && mkdir -p /kubernetes/kubernetes/cfg && mkdir -p /kubernetes/kubernetes/ssl && echo 'export PATH=$PATH:/kubernetes/etcd/bin/:/kubernetes/kubernetes/bin/' >> /etc/profile"
fi

if [ "${2}" == "etcd" ];then
  ansible etcd -i ${1}/etcd_hosts -m shell -a "mkdir -p /kubernetes/etcd/bin && mkdir -p /kubernetes/etcd/cfg && mkdir -p /kubernetes/etcd/ssl && mkdir -p /kubernetes/kubernetes/bin && mkdir -p /kubernetes/kubernetes/cfg && mkdir -p /kubernetes/kubernetes/ssl && mkdir -p /var/lib/etcd && echo 'export PATH=$PATH:/kubernetes/etcd/bin/:/kubernetes/kubernetes/bin/' >> /etc/profile"
fi

if [ "${2}" == "nodes" ];then
  ansible nodes -i ${1}/nodes_hosts -m shell -a "mkdir -p /var/log/kubelet && mkdir -p /var/log/kube-proxy && mkdir -p /kubernetes/etcd/bin && mkdir -p /kubernetes/etcd/cfg && mkdir -p /kubernetes/etcd/ssl && mkdir -p /kubernetes/kubernetes/bin && mkdir -p /kubernetes/kubernetes/cfg && mkdir -p /kubernetes/kubernetes/ssl && echo 'export PATH=$PATH:/kubernetes/etcd/bin/:/kubernetes/kubernetes/bin/' >> /etc/profile"
fi

