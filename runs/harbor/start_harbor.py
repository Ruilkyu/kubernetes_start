"""
时间：2020/6/13
作者：lurui
功能：开始部署harbor

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
import subprocess


def start_harbor():
    basedir = os.path.abspath('.')
    hostspath = basedir + '/ansible/hosts'
    harborpath = hostspath + '/harbor_hosts'

    print("Sir,Starting Start Harbor!")
    try:
        start_harbor = subprocess.check_output(
            '''ansible harbor -i {0} -m shell -a "cd /srv/harbor/ && chmod 777 * && ./install.sh"'''.format(
                harborpath), shell=True)
        print(start_harbor.decode())
    except Exception as e:
        print(e)
    print("Sir,Start Harbor Has Completed!")


# start_harbor()
