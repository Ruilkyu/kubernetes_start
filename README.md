# kubernetes_start
# 二进制kubernetes部署(高可用)
## 一、注意：
```
1、etcd支持1、3、5、7节点
2、master支持1、3节点
3、支持master节点故障恢复
```
准备二进制文件：
```
1、master节点的二进制文件
kube-apiserver、kube-controller-manager、kube-scheduler、kubectl放到deploy/packages/kubernetes/master下
2、node节点的二进制文件
kubelet、kube-proxy放到deploy/packages/kubernetes/nodes下
3、harbor
将解压后的harbor替换deploy/packages/harbor
```
## 二、配置准备
### 1、HARBOR、VIP、SSH、ETCD和MASTER配置信息
#### 1.1、3个master和3个etcd
```
例如：
vi ./cfg/config.ini
[HARBOR]
host=10.10.4.17
port=8088
[VIP]
vip=10.10.1.250
port=8443
virtual_router_id=148
interface=bond0
[SSH]
port=62534
[ETCD]
nums=3
etcd1=10.10.4.18
etcd2=10.10.1.11
etcd3=10.10.1.12
[MASTER]
nums=3
master1=10.10.4.11
master2=10.10.4.12
master3=10.10.4.13
[LABEL]
Key=lotus
Value=node
[RELATED_IP]
cluster_cidr=172.20.0.0/8
service_cluster_ip_range=10.0.0.0/16
cluster_dns=10.0.0.2
[MASTER_RECOVERY]
nums=1
priority1=80
master1=10.10.4.13
```
#### 1.2、1个master和1个etcd(注意：VIP与master相同, port为6443)
```
例如：
vi ./cfg/config.ini
[HARBOR]
host=10.10.4.17
port=8088
[VIP]
vip=10.10.4.11
port=6443
virtual_router_id=148
interface=bond0
[SSH]
port=62534
[ETCD]
nums=1
etcd1=10.10.4.18
[MASTER]
nums=1
master1=10.10.4.11
[LABEL]
Key=lotus
Value=node
[MASTER_RECOVERY]
nums=1
priority1=80
master1=10.10.4.13
```

### 2、nodes列表
```
vi ./cfg/nodes.txt
例如：
10.10.4.15
```

## 三、具体部署
### 1、部署Harbor镜像仓库
```
1.1 生成harbor.yml部署文件
cd ./runs/harbor/ 
python3 start_harbor_yaml.py
1.2 生成harbor的harbor_hosts文件
cd ./runs/harbor/
python3 start_ansible_hosts.py 
1.3 初始化harbor
cd ./runs/init/ 
python3 initenv.py harbor
1.4 启动harbor
cd ./runs/harbor/ 
python3 start_harbor.py
```
### 2、部署Etcd数据库
```
2.1 生成etcd的etcd.j2模版文件
cd ./runs/etcd/ 
python3 start_ansible.py
2.2 生成etcd的etcd_hosts文件
cd ./runs/etcd/ 
python3 start_ansible_hosts.py
2.3 生成etcd对应的server-csr.json文件
cd ./runs/etcd/ 
python3 start_cert.py
2.4 生成etcd对应的network文件
cd ./runs/etcd/ 
python3 start_network.py
2.5 生成etcd对应证书
cd ./runs/certs/ 
python3 gencerts.py etcd
2.6 初始化etcd
cd ./runs/init/ 
python3 initenv.py etcd
2.7 部署etcd
cd ./runs/etcd/ 
python3 start_etcd.py
```
### 3、部署Flanneld网络
```
3.1 生成nodes的nodes_hosts文件
cd ./runs/nodes/ 
python3 start_ansible_hosts.py
3.2 根据提供的etcd列表生成flanneld的配置文件
cd ./runs/flanneld/ 
python3 start_flanneld_cfg.py
3.3 初始化nodes
cd ./runs/init/ 
python3 initenv.py nodes 
3.4 初始化Docker环境
cd ./runs/init/ 
python3 dockerdep.py
3.5 部署flanneld并启动flanneld+docker
cd ./runs/flanneld/ 
python3 start_flanneld.py 
```
### 4、部署Haproxy
```
4.1 生成master的master_hosts文件
cd ./runs/kubernetes/ 
python3 start_ansible_hosts.py
4.2 生成haproxy对应的haproxy.cfg配置文件
cd ./runs/kubernetes/ 
python3 start_haproxy_cfg.py
4.3 在master部署并启动haproxy
cd ./runs/kubernetes/ 
python3 start_haproxy.py
```
### 5、部署Keepalived
```
5.1 生成keepalived对应的keepalived.conf配置文件
cd ./runs/kubernetes/ 
python3 start_keepalived_cfg.py
5.2 在master部署并启动keepalived
cd ./runs/kubernetes/ 
python3 start_keepalived.py 
```
### 6、部署Master
```
6.1 生成master对应的kube-apiserver.j2文件
cd ./runs/kubernetes/ 
python3 start_ansible.py
6.2 生成kubernetes对应的server-csr.json文件
cd ./runs/kubernetes/ 
python3 start_cert.py
6.3 生成master对应证书
cd ./runs/certs/ 
python3 gencerts.py master
6.4 初始化master
cd ./runs/init/ 
python3 initenv.py master
6.5 拷贝Etcd证书
cd ./runs/certs/
python3 copycerts.py master 
6.6 部署master
cd ./runs/kubernetes/ 
python3 start_master.py
```
### 7、部署Nodes
```
7.1 根据提供的vip列表生成nodes的配置文件
cd ./runs/nodes/ 
python3 start_nodes_cfg.py
7.2 生成nodes的认证配置文件
cd ./runs/nodes/cfg/ 
python3 gennodescfg.py
7.3 部署Nodes并启动kubelet、kube-proxy
cd ./runs/nodes/ 
python3 start_nodes.py
```
### 8、Master授权接收到的Nodes请求
```
8.1 向master中写入nodes的对应关系(例如：10.10.52.30 k8s-node52-30)
cd ./runs/domain/ 
python3 start_write_nodes_master.py
8.2 master给nodes授权
cd ./runs/csr/ 
python3 start_csr.py
8.3 master给node打标签
cd ./runs/labels/
python3 start_labels.py
```
### 9、分发基础镜像
```
9.1 pod镜像(registry.cn-hangzhou.aliyuncs.com/google-containers/pause-amd64:3.0)
cd ./runs/images/ 
python3 start_distribute_img.py
```
## 四、总入口
### 1、部署Harbor镜像仓库
```
python3 ./harbor_start.py
```
### 2、部署Etcd数据库集群
```
python3 ./etcd_start.py
```
### 3、部署Master(三节点)
```
python3 ./master_start.py
```
### 4、部署Nodes节点
```
python3 ./nodes_start.py
```
### 5、节点label
```
将cfg目录和label_start.py发送到master节点同一目录
python3 ./label_start.py
```
### 6、修复master节点
```
python3 ./recovery_master_start.py
```
