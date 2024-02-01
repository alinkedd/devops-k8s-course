# devops-k8s-course

Coding tasks and practices for the [course](https://prometheus.org.ua/prometheus-plus/devops_and_kubernetes/)

## Module 3 - Task 4

Key points of the task:
- Use dive utility to optimize image

### Result

https://asciinema.org/a/632450

## Used commands

Check image:

```sh
dive <image_name>
```

Optimize image at 0.9 level:

```sh
dive --ci --lowestEfficiency=0.9 <image_name>
```
