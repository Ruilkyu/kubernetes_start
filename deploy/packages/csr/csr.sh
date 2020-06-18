#!/bin/bash

cd ${1}

/kubernetes/kubernetes/bin/kubectl get csr | grep node-csr | awk '{print $1}' > ./node-csr.txt

csr=`cat node-csr.txt`

for i in $csr
do
      /kubernetes/kubernetes/bin/kubectl certificate approve $i
done