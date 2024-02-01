# devops-k8s-course

Coding tasks and practices for the [course](https://prometheus.org.ua/prometheus-plus/devops_and_kubernetes/)

## Module 5 - Task 1

### Prerequisites

- initial cluster with `kube-system` namespace (e.g. minikube)
- metrics-server:
```sh
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```
or
```sh
minikube addons enable metrics-server
```
- wait a little to have results

### How to use 'kubeplugin'

>NOTE: For the sake of simplicity, we will call it directly.

To use a plugin, make the plugin executable:

```sh
sudo chmod +x ./scripts/kubeplugin
```

To use:

```sh
./scripts/kubeplugin arg1 arg2
```

where arg1 - resource type, arg2 - namespace (by default - kube-system)

### How to get automatically recognized

You should [rename plugin](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/#naming-a-plugin),
e.g. `kubectl-[your_name_here]`. Also, some kind of alias or symlink to
allowed name can be used.

Still make it executable:

```sh
sudo chmod +x ./scripts/kubectl-[your_name_here]
```

and place it anywhere in your PATH:

```sh
sudo mv ./scripts/kubectl-[your_name_here] /usr/local/bin
```

To check that kubectl recognizes your plugin:

```sh
kubectl plugin list
```

To use:

```sh
kubectl [your-name-here] arg1 arg2
```

where arg1 - resource type, arg2 - namespace (by default - kube-system)
