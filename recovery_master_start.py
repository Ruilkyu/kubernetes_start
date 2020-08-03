"""
时间：2020/8/3
作者：lurui
功能：换备机后，master节点修复统一入口
"""

# -*- coding: utf-8 -*-


from runs.kubernetes.start_haproxy_cfg import start_haproxy_cfg
from runs.kubernetes.start_haproxy import start_haproxy
from runs.kubernetes.start_keepalived_cfg import start_keepalived_cfg
from runs.kubernetes.start_keepalived import start_keepalived
from runs.kubernetes.start_ansible import start_ansible
from runs.kubernetes.start_recovery_ansible_hosts import start_recovery_ansible_hosts

from runs.init.initenv import initenv
from runs.certs.copycerts import copycerts
from runs.kubernetes.start_master import start_master

import configparser
import os

basedir = os.path.abspath('.')


def start():
    config = configparser.ConfigParser()
    config.read(basedir + '/cfg/config.ini')
    master_nums = int(config['MASTER']['nums'])

    if master_nums == 1:
        start_ansible()
        start_recovery_ansible_hosts()

        initenv('master')
        copycerts('master')
        start_master()
    else:
        start_ansible()
        start_recovery_ansible_hosts()

        start_haproxy_cfg()
        start_haproxy()
        start_keepalived_cfg()
        start_keepalived()

        initenv('master')
        copycerts('master')
        start_master()


start()
