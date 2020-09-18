"""
时间：2020/8/3
作者：lurui
功能：根据提供的模块列表生成master的ansible模块的master_hosts文件
"""

import os
import configparser


def start_recovery_ansible_hosts():
    basedir = os.path.abspath('.')
    config = configparser.ConfigParser()
    # config.read(basedir + '/cfg/ssh.ini')
    config.read(basedir + '/cfg/config.ini')
    port = config['SSH']['port']
    recovery_master_nums = int(config['MASTER_RECOVERY']['nums'])
    service_cluster_ip_range = config['RELATED_IP']['service_cluster_ip_range']
    cluster_cidr = config['RELATED_IP']['cluster_cidr']

    # master_list = basedir + '/cfg/master.txt'
    # try:
    #     master_list_fh = open(master_list, mode="r", encoding='utf-8')
    # except FileNotFoundError:
    #     os.mknod(master_list)
    #     master_list_fh = open(master_list, mode="r", encoding='utf-8')

    master_ansible_hosts_templates = basedir + '/templates/kubernetes/ansible/recovery_hosts/{0}.yaml'.format(
        recovery_master_nums)
    try:
        master_ansible_hosts_templates_fh = open(master_ansible_hosts_templates, mode="r", encoding='utf-8')
    except FileNotFoundError:
        os.mknod(master_ansible_hosts_templates)
        master_ansible_hosts_templates_fh = open(master_ansible_hosts_templates, mode="r", encoding='utf-8')

    if os.path.exists(basedir + '/ansible/hosts/master_hosts'):
        os.remove(basedir + '/ansible/hosts/master_hosts')

    if not os.path.exists(basedir + '/ansible/hosts'):
        os.makedirs(basedir + '/ansible/hosts')

    master_ansible_hosts_data = ''
    try:
        for k in master_ansible_hosts_templates_fh.readlines():
            master_ansible_hosts_data += k
    except Exception as e:
        print(e)

    try:
        location = basedir + '/ansible/hosts/master_hosts'
        file = open(location, 'a')

        # masterlist = []
        #
        # for l in master_list_fh.readlines():
        #     masterlist.append(l.strip("\n"))

        resultdate = ""
        if recovery_master_nums == 1:
            master1 = config['MASTER_RECOVERY']['master1']
            priority1 = config['MASTER_RECOVERY']['priority1']
            resultdate = master_ansible_hosts_data.format(master1, port, priority1, service_cluster_ip_range, cluster_cidr)
        elif recovery_master_nums == 2:
            master1 = config['MASTER_RECOVERY']['master1']
            master2 = config['MASTER_RECOVERY']['master2']
            priority1 = config['MASTER_RECOVERY']['priority1']
            priority2 = config['MASTER_RECOVERY']['priority2']
            resultdate = master_ansible_hosts_data.format(master1, master2, port, priority1, priority2,
                                                          service_cluster_ip_range, cluster_cidr)
        elif recovery_master_nums == 3:
            master1 = config['MASTER_RECOVERY']['master1']
            master2 = config['MASTER_RECOVERY']['master2']
            master3 = config['MASTER_RECOVERY']['master3']
            priority1 = config['MASTER_RECOVERY']['priority1']
            priority2 = config['MASTER_RECOVERY']['priority2']
            priority3 = config['MASTER_RECOVERY']['priority3']
            resultdate = master_ansible_hosts_data.format(master1, master2, master3, port, priority1, priority2,
                                                          priority3, service_cluster_ip_range, cluster_cidr)

        # resultdate = ""
        # resultdate = master_ansible_hosts_data.format(master1, master2, master3, port)
        # resultdate = master_ansible_hosts_data.format(masterlist[0], masterlist[1], masterlist[2], port)

        file.write(resultdate)
        file.close()
    except Exception as e:
        print(e)

# start_ansible_hosts()
