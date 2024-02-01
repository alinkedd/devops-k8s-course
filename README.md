# devops-k8s-course

Coding tasks and practices for the [course](https://prometheus.org.ua/prometheus-plus/devops_and_kubernetes/)

## Module 3 - Task with manual check

Key points of the task:

- Run the steps to init container specification: 
```
runc spec
```
- Add network configuration for your container spec file
- Setup network interfaces to reproduce the issue
- Share the recording URL by running asciinema

### Result

[https://asciinema.org/a/632444](https://asciinema.org/a/632444)

## Used commands (distinct local session)

Create demo folder to have files:

```sh
mkdir demo && cd demo/
```

Create container config and its root filesystem:

```sh
runc spec
```

Update config as following:

- background mode:
  ```json
  "terminal": false
  ```
- http-server imitation:
  ```json
  "args": [
    "sh", "-c", "while true; do { echo -e 'HTTP/1.1 200 OK\n\n Version 1.0.0'; } | nc -vlp 8080; done"
  ]
  ```
- network namespace:
  ```json
  {
    "type": "network",
    "path": "/var/run/netns/runc"
  }
  ```

Create `runc` network namespace:

```sh
sudo ip netns add runc
```

Install `bridge-utils` if needed:

```sh
sudo apt-get update
sudo apt-get install bridge-utils
```

Setup network via bridge (in `root` mode):

```sh
# Create a new Ethernet bridge named runc0
brctl addbr runc0

# Activate the runc0 bridge, enabling it to pass traffic
ip link set runc0 up

# Assign an IP address (192.168.0.1/24) to the runc0 bridge
ip addr add 192.168.0.1/24 dev runc0

# Create a pair of connected virtual Ethernet devices (veth pairs) - veth-host
# and veth-guest
ip link add name veth-host type veth peer name veth-guest

# Bring up the veth-host interface, making it ready to pass traffic
ip link set veth-host up

# Add the veth-host end of the virtual Ethernet pair to the runc0 bridge
brctl addif runc0 veth-host

# Moves the veth-guest interface into a separate network namespace named runc
ip link set veth-guest netns runc

# Rename veth-guest to eth1 within the runc network namespace
ip netns exec runc ip link set veth-guest name eth1

# Assign an IP address (192.168.0.2/24) to the eth1 interface within the runc
# namespace
ip netns exec runc ip addr add 192.168.0.2/24 dev eth1

# Activate the eth1 interface within the runc namespace
ip netns exec runc ip link set eth1 up

# Set the default gateway for the runc namespace to be 192.168.0.1, which is
# the IP address of the runc0 bridge in the main network namespace. This allows
# traffic from the runc namespace to reach external networks via the bridge.
ip netns exec runc ip route add default via 192.168.0.1
```

Create and run container with `demo` name:

```sh
sudo runc run demo
```

Check that container is accessible:

```sh
curl 192.168.0.2:8080
```

Terminate container:

```sh
sudo runc kill demo KILL
```
