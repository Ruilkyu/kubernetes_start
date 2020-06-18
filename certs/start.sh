#!/bin/bash

cd ${1}

./prepare.sh

if [ ${2} == 'etcd' ];then
  cd ./etcd && /usr/local/bin/cfssl gencert -initca ca-csr.json | /usr/local/bin/cfssljson -bare ca - &&  /usr/local/bin/cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=etcd server-csr.json | /usr/local/bin/cfssljson -bare server
fi

if [ ${2} == 'master' ];then
  cd ./kubernetes && /usr/local/bin/cfssl gencert -initca ca-csr.json | /usr/local/bin/cfssljson -bare ca - && /usr/local/bin/cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=kubernetes server-csr.json | /usr/local/bin/cfssljson -bare server  && /usr/local/bin/cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=kubernetes kube-proxy-csr.json | /usr/local/bin/cfssljson -bare kube-proxy
fi