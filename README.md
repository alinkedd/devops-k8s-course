# devops-k8s-course

Coding tasks and practices for the [course](https://prometheus.org.ua/prometheus-plus/devops_and_kubernetes/)

## Module 1 - Task 2

Key points of the task:
- Repeat «Build, Ship, Run» coding session to create an app, its image and container, and the k3s cluster

### Result

- code works
- [image at docker hub](https://hub.docker.com/repository/docker/alinkedd/do-k8s-m1-t2/general)
- local cluster also works

## How to use

### Prerequisites

- Go
- [Docker](https://docs.docker.com/get-docker/) >= v20.10.5 
- [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
- [k3d](https://k3d.io/v5.6.0/) with [k3s](https://github.com/k3s-io/k3s)

### Commands

Build:

```sh
go build -o bin/app src/main.go
```

Run:
```sh
bin/app
```

App runs at [localhost:8080](http://localhost:8080)

Docker image: https://hub.docker.com/r/alinkedd/do-k8s-m1-t2

## Used k8s commands index

Create cluster:

```sh
k3d cluster create <cluster-name>
```

List clusters:

```sh
k3d cluster list
```

Remove cluster:

```sh
k3d cluster delete <cluster-name>
```

***

Create deployment using image from Docker Hub:

```sh
kubectl create deploy <cluster-name> --image <image-name>
```
, where `<image-name>` is `<user>/<container-name>:<version>` tag.

Forward local port:

```sh
kubectl port-forward deploy/<cluster-name> <port>
```

Zero-downtime deployment to update image:

```sh
kubectl set image deploy <cluster-name> <container-name>=<image-name>
```

, where `<image-name>` contains same container with higher version.

***

Print info about environment and configuration:

```sh
kubectl cluster-info
```

Print info about deployment as table with additional columns:

```sh
kubectl get deploy <cluster-name> -o wide
```

Watch info about pods:

```sh
kubectl get po -w
```
