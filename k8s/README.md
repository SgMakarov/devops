# K8s manifests

Since I have added a helm chart on a first lab, all I had to
do is to run `helm template --output-dir` on this chart to
obtain k8s manifests. I adjusted values to have latest
version of image and 3 replicas, as well as no ingress for
local tests.

The output is the following:

```sh
$ kubectl get po,svc -n devops-labs
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-854b5b5d8d-2kmkz   1/1     Running   0          7m50s
pod/python-app-854b5b5d8d-4t9cw   1/1     Running   0          7m59s
pod/python-app-854b5b5d8d-mcnm7   1/1     Running   0          7m49s

NAME               TYPE         CLUSTER-IP    EXTERNAL-IP  PORT(S)        AGE
service/python-app LoadBalancer 10.102.249.24 <pending>    5000:30455/TCP 16m
```

## Bonus

1. I do not have extra app, but all I have to change is image and ports.

1. Explanations:

    a. Ingress - some kind of http proxy, that routes traffic
    to a service or services depending on path. It also
    serves SSL certs. I have an example in my helm chart
    with nginx ingress controller and cert-manager.

    b. Ingress controller - ingress itself is just an
    abstraction, the actual routing and ssl management is
    done by some webserver (nginx, traefik, envoy). Those is
    called ingress controller.

    c. StatefulSet - similar to the Deployment we made, but
    for stateful applications. If in deployment failed
    rescheduled pod is simply recreated as a new one,
    StatefulSet makes sure this new pod will have the sam
     identifiers, hostnames, PVs.

    d. DaemonSet - an application that ensures some system
    (or user defined) pods are present on each node.

    e. PersistentVolume - in docker we have volumes to map
    some folder into a host machine, so that data is not lost
    with container. In k8s we have multiple nodes, so we
    can't rely on mapping into a node, the node can be
    changed in a while. Instead PVs are mapped from some VPC
    disks directly to a container, there is no dependency on
    host.
