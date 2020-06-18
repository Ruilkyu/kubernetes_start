"""
时间：2020/6/13
时间：2020/6/15 修改调整：取消传priority参数，只传vip
作者：lurui
功能：根据提供的模版，生成keepalived对应的keepalived.conf配置文件

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')

时间：2020/6/18
作者：lurui
修改：增加keepalived的interface配置读取
"""

import os
import configparser


def start_keepalived_cfg():
    basedir = os.path.abspath('.')
    config = configparser.ConfigParser()
    # config.read(basedir + '/cfg/vip.ini')
    config.read(basedir + '/cfg/config.ini')
    vip = config['VIP']['vip']
    virtual_router_id = config['VIP']['virtual_router_id']
    interface = config['VIP']['interface']

    keepalived_templates = basedir + '/templates/keepalived/keepalived.yaml'
    try:
        keepalived_templates_fh = open(keepalived_templates, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(keepalived_templates)
        keepalived_templates_fh = open(keepalived_templates, mode="r", encoding='utf-8')

    if os.path.exists(basedir + '/deploy/keepalived/cfg/keepalived.conf.j2'):
        os.remove(basedir + '/deploy/keepalived/cfg/keepalived.conf.j2')

    # if os.path.exists(basedir + '/deploy/keepalived/cfg/keepalived1.conf'):
    #     os.remove(basedir + '/deploy/keepalived/cfg/keepalived1.conf')
    #
    # if os.path.exists(basedir + '/deploy/keepalived/cfg/keepalived2.conf'):
    #     os.remove(basedir + '/deploy/keepalived/cfg/keepalived2.conf')
    #
    # if os.path.exists(basedir + '/deploy/keepalived/cfg/keepalived3.conf'):
    #     os.remove(basedir + '/deploy/keepalived/cfg/keepalived3.conf')

    if not os.path.exists(basedir + '/deploy/keepalived/cfg'):
        os.makedirs(basedir + '/deploy/keepalived/cfg')

    # keepalived1_data = ''
    # keepalived2_data = ''
    # keepalived3_data = ''

    keepalived_data = ''
    try:
        for k in keepalived_templates_fh.readlines():
            # keepalived1_data += k
            # keepalived2_data += k
            # keepalived3_data += k
            keepalived_data += k
    except Exception as e:
        print(e)

    # try:
    #     location = basedir + '/deploy/keepalived/cfg/keepalived1.conf'
    #     file = open(location, 'a')
    #
    #     resultdate = ""
    #     resultdate = keepalived1_data.format(100, vip)
    #
    #     file.write(resultdate)
    #     file.close()
    # except Exception as e:
    #     print(e)
    #
    # try:
    #     location = basedir + '/deploy/keepalived/cfg/keepalived2.conf'
    #     file = open(location, 'a')
    #
    #     resultdate = ""
    #     resultdate = keepalived2_data.format(90, vip)
    #
    #     file.write(resultdate)
    #     file.close()
    # except Exception as e:
    #     print(e)
    #
    # try:
    #     location = basedir + '/deploy/keepalived/cfg/keepalived3.conf'
    #     file = open(location, 'a')
    #
    #     resultdate = ""
    #     resultdate = keepalived3_data.format(80, vip)
    #
    #     file.write(resultdate)
    #     file.close()
    # except Exception as e:
    #     print(e)

    try:
        location = basedir + '/deploy/keepalived/cfg/keepalived.conf.j2'
        file = open(location, 'a')

        resultdate = ""
        resultdate = keepalived_data.format(vip, virtual_router_id, interface)

        file.write(resultdate)
        file.close()
    except Exception as e:
        print(e)


# start_keepalived_cfg()
