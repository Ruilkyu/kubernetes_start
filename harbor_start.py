"""
时间：2020/6/17
作者：lurui
功能：harbor统一入口
"""

# -*- coding: utf-8 -*-

from runs.harbor.start_harbor_yaml import start_harbor_yaml
from runs.harbor.start_ansible_hosts import start_ansible_hosts
from runs.init.initenv import initenv
from runs.harbor.start_harbor import start_harbor


def start():
    start_harbor_yaml()
    start_ansible_hosts()
    initenv('harbor')
    start_harbor()


start()
