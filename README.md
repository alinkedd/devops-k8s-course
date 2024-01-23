# devops-k8s-course

Coding tasks and practices for the [course](https://prometheus.org.ua/prometheus-plus/devops_and_kubernetes/)

## Week 5 - Task 3

Key points of the task:
- Create yml kubernetes manifests using [AI prompts via kubectl plugin](https://github.com/sozercan/kubectl-ai)
- Test at local cluster

### Result

https://github.com/alinkedd/godabot-infra/commit/7bff0046604b23997ea12ca33a3cf1191a0cd9f1

## Used commands

To generate `yml` file:

```sh
kubectl ai "generate basic pod yml file" --raw > ./yaml/app.yaml && code ./yaml/app.yaml
```
