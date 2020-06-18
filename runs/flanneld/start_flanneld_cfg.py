"""
时间：2020/6/12
作者：lurui
功能：根据提供的etcd列表生成flanneld的配置文件

时间：2020/6/16
作者：lurui
修改：系统传参数方式改为读配置文件,读etcd.txt文件改为读config.ini

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
# import sys
import configparser


# etcd_nums = int(sys.argv[1])


def start_flanneld_cfg():
    basedir = os.path.abspath('.')
    config = configparser.ConfigParser()
    config.read(basedir + '/cfg/config.ini')
    etcd_nums = int(config['ETCD']['nums'])
    # etcd_list = basedir + '/cfg/etcd.txt'
    # try:
    #     etcd_list_fh = open(etcd_list, mode="r", encoding='utf-8')
    # except FileNotFoundError:
    #     os.mknod(etcd_list)
    #     etcd_list_fh = open(etcd_list, mode="r", encoding='utf-8')

    flanneld_cfg_templates = basedir + '/templates/flanneld/{0}.yaml'.format(etcd_nums)
    try:
        flanneld_cfg_templates_fh = open(flanneld_cfg_templates, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(flanneld_cfg_templates)
        flanneld_cfg_templates_fh = open(flanneld_cfg_templates, mode="r", encoding='utf-8')

    if os.path.exists(basedir + '/deploy/flanneld/cfg/flanneld'):
        os.remove(basedir + '/deploy/flanneld/cfg/flanneld')

    if not os.path.exists(basedir + '/deploy/flanneld/cfg'):
        os.makedirs(basedir + '/deploy/flanneld/cfg')

    flanneld_cfg_data = ''
    try:
        for k in flanneld_cfg_templates_fh.readlines():
            flanneld_cfg_data += k
    except Exception as e:
        print(e)

    try:
        location = basedir + '/deploy/flanneld/cfg/flanneld'
        file = open(location, 'a')

        # etcdlist = []
        #
        # for l in etcd_list_fh.readlines():
        #     etcdlist.append(l.strip("\n"))

        resultdate = ""
        if etcd_nums == 1:
            etcd1 = config['ETCD']['etcd1']
            resultdate = flanneld_cfg_data.format(etcd1)
        elif etcd_nums == 3:
            etcd1 = config['ETCD']['etcd1']
            etcd2 = config['ETCD']['etcd2']
            etcd3 = config['ETCD']['etcd3']
            resultdate = flanneld_cfg_data.format(etcd1, etcd2, etcd3)
        elif etcd_nums == 5:
            etcd1 = config['ETCD']['etcd1']
            etcd2 = config['ETCD']['etcd2']
            etcd3 = config['ETCD']['etcd3']
            etcd4 = config['ETCD']['etcd4']
            etcd5 = config['ETCD']['etcd5']
            resultdate = flanneld_cfg_data.format(etcd1, etcd2, etcd3, etcd4, etcd5)
        elif etcd_nums == 7:
            etcd1 = config['ETCD']['etcd1']
            etcd2 = config['ETCD']['etcd2']
            etcd3 = config['ETCD']['etcd3']
            etcd4 = config['ETCD']['etcd4']
            etcd5 = config['ETCD']['etcd5']
            etcd6 = config['ETCD']['etcd6']
            etcd7 = config['ETCD']['etcd7']
            resultdate = flanneld_cfg_data.format(etcd1, etcd2, etcd3, etcd4, etcd5, etcd6, etcd7)

        # if etcd_nums == 1:
        #     resultdate = flanneld_cfg_data.format(etcdlist[0])
        # elif etcd_nums == 3:
        #     resultdate = flanneld_cfg_data.format(etcdlist[0], etcdlist[1], etcdlist[2])
        # elif etcd_nums == 5:
        #     resultdate = flanneld_cfg_data.format(etcdlist[0], etcdlist[1], etcdlist[2], etcdlist[3], etcdlist[4])
        # elif etcd_nums == 7:
        #     resultdate = flanneld_cfg_data.format(etcdlist[0], etcdlist[1], etcdlist[2], etcdlist[3], etcdlist[4],
        #                                           etcdlist[5], etcdlist[6])

        file.write(resultdate)
        file.close()
    except Exception as e:
        print(e)


# start_flanneld_cfg()
