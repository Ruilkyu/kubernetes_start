"""
时间：2020/6/17
作者：lurui
功能：etcd统一入口
"""

# -*- coding: utf-8 -*-

from runs.etcd.start_ansible import start_ansible
from runs.etcd.start_ansible_hosts import start_ansible_hosts
from runs.etcd.start_cert import start_cert
from runs.etcd.start_network import start_network
from runs.certs.gencerts import gencerts
from runs.init.initenv import initenv
from runs.etcd.start_etcd import start_etcd


def start():
    start_ansible()
    start_ansible_hosts()
    start_cert()
    start_network()
    gencerts('etcd')
    initenv('etcd')
    start_etcd()


start()
