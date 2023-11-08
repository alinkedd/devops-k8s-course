# devops-k8s-course

Coding tasks and practices for the [course](https://prometheus.org.ua/prometheus-plus/devops_and_kubernetes/)

## Module 2 - Task 2

Print object ID of the file and write object to the object database:
```sh
echo $(git hash-object -w <file>)
```

Print content of the object by its name, e.g. `<sha1>`:
```sh
git cat-file -p <name>
```

Add new file to index and register its content:
```sh
git update-index --add <file>
```

Show information about staged files:
```sh
git ls-files --stage
```
