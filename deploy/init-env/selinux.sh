#!/bin/bash
if [ "${2}" == "master" ];then
  ansible master -i ${1}/master_hosts -m shell -a "echo > /etc/selinux/config && echo SELINUX=disabled >> /etc/selinux/config && echo SELINUXTYPE=targeted >> /etc/selinux/config"
fi

if [ "${2}" == "etcd" ];then
  ansible etcd -i ${1}/etcd_hosts -m shell -a "echo > /etc/selinux/config && echo SELINUX=disabled >> /etc/selinux/config && echo SELINUXTYPE=targeted >> /etc/selinux/config"
fi

if [ "${2}" == "nodes" ];then
  ansible nodes -i ${1}/nodes_hosts -m shell -a "echo > /etc/selinux/config && echo SELINUX=disabled >> /etc/selinux/config && echo SELINUXTYPE=targeted >> /etc/selinux/config"
fi

if [ "${2}" == "harbor" ];then
  ansible harbor -i ${1}/harbor_hosts -m shell -a "echo > /etc/selinux/config && echo SELINUX=disabled >> /etc/selinux/config && echo SELINUXTYPE=targeted >> /etc/selinux/config"
fi
