# devops-k8s-course

Coding tasks and practices for the [course](https://prometheus.org.ua/prometheus-plus/devops_and_kubernetes/)

## Module 5 - Task 4

Key points of the task:
- setup given app
- per given request, debug app version upgrade as this command is not sufficient:
  ```sh
  helm template new-version ./helm -s templates/api-deploy.yaml --set image.tag=build-802e329
  ```
- allow only qa team to access endpoint of the new version

### Result

[./result.txt](./result.txt)

## Used commands

### App setup

- clone repo:
  ```sh
  git clone --depth=1 https://github.com/den-vasyliev/go-demo-app.git
  ```
- install app in the cluster using helm:
  ```sh
  helm install current-version ./helm
  ```
- forward port ambassador service:
  ```sh
  kubectl port-forward svc/ambassador 8080:80
  ```
- get current version `k8sdiy-api:599e1af`:
  ```sh
  curl localhost:8080/api/
  ```

### Debugging

Firstly, template should be applied to cluster using `| kubectl apply -f -` at
the end.

Secondly, we can see issues with container creating by using `kubectl describe`
command. By given info, we can understand that secret and configmap should be
updated as well as a service.

Finally, to provide access only for the qa, api header should be set to `qa`
and canary should be set to `100`.
