#!/bin/bash

cd ${1}

./prepare.sh ${2} ${3}
./selinux.sh ${2} ${3}
./firewalld.sh ${2} ${3}
./swap.sh ${2} ${3}
