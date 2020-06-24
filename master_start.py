"""
时间：2020/6/17
作者：lurui
功能：master统一入口

时间：2020/6/24
作者：lurui
功能：master各模块启动顺序，优先生成master_hosts
"""

# -*- coding: utf-8 -*-


from runs.kubernetes.start_haproxy_cfg import start_haproxy_cfg
from runs.kubernetes.start_haproxy import start_haproxy
from runs.kubernetes.start_keepalived_cfg import start_keepalived_cfg
from runs.kubernetes.start_keepalived import start_keepalived
from runs.kubernetes.start_ansible import start_ansible
from runs.kubernetes.start_ansible_hosts import start_ansible_hosts
from runs.kubernetes.start_cert import start_cert
from runs.certs.gencerts import gencerts
from runs.init.initenv import initenv
from runs.certs.copycerts import copycerts
from runs.kubernetes.start_master import start_master


def start():
    start_ansible()
    start_ansible_hosts()
    start_cert()
    gencerts('master')

    start_haproxy_cfg()
    start_haproxy()
    start_keepalived_cfg()
    start_keepalived()

    initenv('master')
    copycerts('master')
    start_master()


start()
