"""
时间：2020/6/13
作者：lurui
功能：生成harbor部署文件

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
import configparser


def start_harbor_yaml():
    basedir = os.path.abspath('.')
    config = configparser.ConfigParser()
    # config.read(basedir + '/cfg/harbor.ini')
    config.read(basedir + '/cfg/config.ini')
    host = config['HARBOR']['host']
    port = config['HARBOR']['port']

    harbor_yml_templates = basedir + '/templates/harbor/harbor.yaml'
    docker_daemon_templates = basedir + '/templates/docker/daemon.yaml'

    try:
        harbor_yml_templates_fh = open(harbor_yml_templates, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(harbor_yml_templates)
        harbor_yml_templates_fh = open(harbor_yml_templates, mode="r", encoding='utf-8')

    try:
        docker_daemon_templates_fh = open(docker_daemon_templates, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(docker_daemon_templates)
        docker_daemon_templates_fh = open(docker_daemon_templates, mode="r", encoding='utf-8')

    if os.path.exists(basedir + '/deploy/packages/kubernetes/nodes/daemon.json'):
        os.remove(basedir + '/deploy/packages/kubernetes/nodes/daemon.json')

    if not os.path.exists(basedir + '/deploy/packages/kubernetes/nodes'):
        os.makedirs(basedir + '/deploy/packages/kubernetes/nodes')

    harbor_yml_data = ''
    docker_daemon_data = ''
    try:
        for k in harbor_yml_templates_fh.readlines():
            harbor_yml_data += k
    except Exception as e:
        print(e)

    try:
        for k in docker_daemon_templates_fh.readlines():
            docker_daemon_data += k
    except Exception as e:
        print(e)

    if os.path.exists(basedir + '/deploy/packages/harbor/harbor.yml'):
        os.remove(basedir + '/deploy/packages/harbor/harbor.yml')

    if not os.path.exists(basedir + '/deploy/packages/harbor'):
        os.makedirs(basedir + '/deploy/packages/harbor')

    try:
        location = basedir + '/deploy/packages/harbor/harbor.yml'
        file = open(location, 'a')

        resultdate = ""
        resultdate = harbor_yml_data.format(host, port)
        file.write(resultdate)
        file.close()
    except Exception as e:
        print(e)

    try:
        location = basedir + '/deploy/packages/kubernetes/nodes/daemon.json'
        file = open(location, 'a')

        resultdate = ""
        resultdate = docker_daemon_data.format(host, port)
        file.write(resultdate)
        file.close()
    except Exception as e:
        print(e)

# start_harbor_yaml()
