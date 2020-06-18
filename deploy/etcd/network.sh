/kubernetes/etcd/bin/etcdctl --ca-file=/kubernetes/etcd/ssl/ca.pem --cert-file=/kubernetes/etcd/ssl/server.pem --key-file=/kubernetes/etcd/ssl/server-key.pem \
 --endpoints='https://10.10.4.18:2379,https://10.10.1.11:2379,https://10.10.1.12:2379' \
 set /coreos.com/network/config  \
 '{ "Network": "172.20.0.0/8", "Backend": {"Type": "host-gw"}}'