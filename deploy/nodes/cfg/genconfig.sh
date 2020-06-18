#!/bin/bash

cd ${1} && bash environment.sh && bash envkubelet.kubeconfig.sh && bash env_proxy.sh