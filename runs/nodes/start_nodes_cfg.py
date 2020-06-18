"""
时间：2020/6/12
作者：lurui
功能：根据提供的vip列表生成nodes的配置文件

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
import configparser


def start_nodes_cfg():
    basedir = os.path.abspath('.')
    config = configparser.ConfigParser()
    # config.read(basedir + '/cfg/vip.ini')
    config.read(basedir + '/cfg/config.ini')
    vip = config['VIP']['vip']
    port = config['VIP']['port']

    nodes_cfg_env_proxy_templates = basedir + '/templates/kubernetes/nodes/cfg/env_proxy.yaml'
    nodes_cfg_environment_templates = basedir + '/templates/kubernetes/nodes/cfg/environment.yaml'
    nodes_cfg_envkubelet_kubeconfig_templates = basedir + '/templates/kubernetes/nodes/cfg/envkubelet.kubeconfig.yaml'

    # env_proxy.sh
    try:
        nodes_cfg_env_proxy_templates_fh = open(nodes_cfg_env_proxy_templates, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(nodes_cfg_env_proxy_templates)
        nodes_cfg_env_proxy_templates_fh = open(nodes_cfg_env_proxy_templates, mode="r", encoding='utf-8')
    # environment.sh
    try:
        nodes_cfg_environment_templates_fh = open(nodes_cfg_environment_templates, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(nodes_cfg_environment_templates)
        nodes_cfg_environment_templates_fh = open(nodes_cfg_environment_templates, mode="r", encoding='utf-8')
    # envkubelet.kubeconfig.sh
    try:
        nodes_cfg_envkubelet_kubeconfig_templates_fh = open(nodes_cfg_envkubelet_kubeconfig_templates, mode="r",
                                                            encoding='utf-8')
    except FileNotFoundError:
        os.mknod(nodes_cfg_envkubelet_kubeconfig_templates)
        nodes_cfg_envkubelet_kubeconfig_templates_fh = open(nodes_cfg_envkubelet_kubeconfig_templates, mode="r",
                                                            encoding='utf-8')

    if os.path.exists(basedir + '/deploy/nodes/cfg/env_proxy.sh'):
        os.remove(basedir + '/deploy/nodes/cfg/env_proxy.sh')

    if os.path.exists(basedir + '/deploy/nodes/cfg/environment.sh'):
        os.remove(basedir + '/deploy/nodes/cfg/environment.sh')

    if os.path.exists(basedir + '/deploy/nodes/cfg/envkubelet.kubeconfig.sh'):
        os.remove(basedir + '/deploy/nodes/cfg/envkubelet.kubeconfig.sh')

    if not os.path.exists(basedir + '/deploy/nodes/cfg'):
        os.makedirs(basedir + '/deploy/nodes/cfg')

    nodes_cfg_env_proxy_data = ''
    try:
        for k in nodes_cfg_env_proxy_templates_fh.readlines():
            nodes_cfg_env_proxy_data += k
    except Exception as e:
        print(e)

    nodes_cfg_environment_data = ''
    try:
        for k in nodes_cfg_environment_templates_fh.readlines():
            nodes_cfg_environment_data += k
    except Exception as e:
        print(e)

    nodes_cfg_envkubelet_kubeconfig_data = ''
    try:
        for k in nodes_cfg_envkubelet_kubeconfig_templates_fh.readlines():
            nodes_cfg_envkubelet_kubeconfig_data += k
    except Exception as e:
        print(e)

    try:
        location = basedir + '/deploy/nodes/cfg/env_proxy.sh'
        file = open(location, 'a')

        resultdate = ""
        resultdate = nodes_cfg_env_proxy_data.format(vip, port)

        file.write(resultdate)
        file.close()
    except Exception as e:
        print(e)

    try:
        location = basedir + '/deploy/nodes/cfg/environment.sh'
        file = open(location, 'a')

        resultdate = ""
        resultdate = nodes_cfg_environment_data.format(vip, port)

        file.write(resultdate)
        file.close()
    except Exception as e:
        print(e)

    try:
        location = basedir + '/deploy/nodes/cfg/envkubelet.kubeconfig.sh'
        file = open(location, 'a')

        resultdate = ""
        resultdate = nodes_cfg_envkubelet_kubeconfig_data.format(vip, port)

        file.write(resultdate)
        file.close()
    except Exception as e:
        print(e)


# start_nodes_cfg()
