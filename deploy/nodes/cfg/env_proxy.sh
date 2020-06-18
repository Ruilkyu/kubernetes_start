BOOTSTRAP_TOKEN=aada73279ef0b04e039d2817e33fcf65
KUBE_APISERVER="https://10.10.1.250:8443"

./kubectl config set-cluster kubernetes \
  --certificate-authority=../../../certs/kubernetes/ca.pem \
  --embed-certs=true \
  --server=${KUBE_APISERVER} \
  --kubeconfig=kube-proxy.kubeconfig

./kubectl config set-credentials kube-proxy \
  --client-certificate=../../../certs/kubernetes/kube-proxy.pem \
  --client-key=../../../certs/kubernetes/kube-proxy-key.pem \
  --embed-certs=true \
  --kubeconfig=kube-proxy.kubeconfig

./kubectl config set-context default \
  --cluster=kubernetes \
  --user=kube-proxy \
  --kubeconfig=kube-proxy.kubeconfig

./kubectl config use-context default --kubeconfig=kube-proxy.kubeconfig
