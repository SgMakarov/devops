# Helm chart

I wrote this helm chart quite a long time ago. It is not perfect,
as it does not have healthchecks, resources for pod etc. It also has
some hardcoded things. However, this was just fine almost always I
wanted to deploy one-container app.

## Outputs

```sh
$ kubectl get po,svc -n devops-helm
NAME                             READY   STATUS    RESTARTS   AGE
pod/python-app-5df8f47f8-6dkl9   1/1     Running   0          28s
pod/python-app-5df8f47f8-9hjw8   1/1     Running   0          28s
pod/python-app-5df8f47f8-dvqhq   1/1     Running   0          28s

NAME               TYPE         CLUSTER-IP   EXTERNAL-IP PORT(S)          AGE
service/python-app LoadBalancer 10.98.92.222 <pending>   5000:31468/TCP   28s
```

## Bonus

1. No need for extra chart, just change values instead. This is why helm
    is better than bare manifests - go templates allow not to change
    tons of files to customize deployment, just change `values.yaml`.

1. This is a tool not to write templates for some common things each time.
    For example, you have multiple services with different architectures,
    each has multiple pods. It will be hard to create a generic chart for
    all of them, and `values.yaml` will be gigantic. However, you can create
    a library charts for some common things, for example, for ingress template.
