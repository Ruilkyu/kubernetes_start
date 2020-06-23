"""
时间：2020/6/17
作者：lurui
功能：nodes统一入口

时间：2020/6/18
作者：lurui
功能：node各模块启动顺序，优先生成nodes_hosts
"""

# -*- coding: utf-8 -*-
import time

from runs.flanneld.start_flanneld_cfg import start_flanneld_cfg
from runs.init.initenv import initenv
from runs.init.dockerdep import dockerdep
from runs.flanneld.start_flanneld import start_flanneld
from runs.nodes.start_nodes_cfg import start_nodes_cfg
from runs.nodes.start_ansible_hosts import start_ansible_hosts
from runs.nodes.cfg.gennodescfg import gennodescfg
from runs.nodes.start_nodes import start_nodes
from runs.domain.start_write_nodes_master import start_write_nodes_master
from runs.csr.start_csr import start_csr
from runs.images.start_distribute_img import start_distribute_img
from runs.labels.start_labels import start_labels_nodes


def start():
    start_nodes_cfg()
    start_ansible_hosts()
    gennodescfg()

    start_flanneld_cfg()
    initenv('nodes')
    dockerdep()
    start_flanneld()

    start_nodes()

    time.sleep(3)
    start_write_nodes_master()
    start_csr()
    start_distribute_img()
    start_labels_nodes()


start()
