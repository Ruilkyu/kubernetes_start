"""
时间：2020/6/15
作者：lurui
功能：master给nodes授权

时间：2020/6/17
作者：lurui
修改：基路径 basedir = os.path.dirname(os.path.dirname(os.getcwd()))，改为调用者路径 basedir = os.path.abspath('.')
"""

import os
import subprocess


def start_csr():
    basedir = os.path.abspath('.')
    cfgpath = basedir + '/deploy/packages/csr'
    masterpath = basedir + '/ansible/hosts/master_hosts'

    print("BOSS,Starting Copy CSR Scripts!")
    try:
        copy_csr_sh = subprocess.check_output(
            '''ansible master -i {0} -m copy -a "src={1}/csr.sh dest=/tmp/"'''.format(masterpath, cfgpath), shell=True)
        print(copy_csr_sh.decode())
        add_nodes_cfg = subprocess.check_output(
            '''ansible master -i {0} -m shell -a "cd /tmp/ && chmod +x csr.sh && ./csr.sh"'''.format(
                masterpath), shell=True)
        print(add_nodes_cfg.decode())
    except Exception as e:
        print(e)
    print("BOSS,Copy CSR Scripts Has Completed!")

# start_csr()
