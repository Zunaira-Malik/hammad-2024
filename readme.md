# LarkSuite Kubernetes Deployment

This repository contains the necessary files to deploy the `LarkSuite` application on a Kubernetes cluster using `kubeadm`. The application is packaged as a Docker image and deployed using Kubernetes manifests.

## Prerequisites

- Docker
- Kubernetes tools: `kubeadm`, `kubectl`, `kubelet`
- At least 2 Virtual Machines (1 master and 1 worker node)
- Ingress Controller

## Cluster Setup Using kubeadm

### Step 1: Install Docker

Install Docker on all the nodes (master and worker nodes) to run containerized applications.

```bash
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
```bash

### Step 2: Install Kubernetes Tools

Install kubeadm, kubectl, and kubelet on all nodes.

```bash
sudo apt-get update
sudo apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```bash

### Step 3: Initialize the Master Node

On the master node, initialize the Kubernetes cluster using kubeadm.

```bash
sudo kubeadm init --pod-network-cidr=192.168.0.0/16
```bash

Set up kubectl access for the ubuntu user:

```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```bash

### Step 4: Install a Pod Network (e.g., Calico)

Install a network add-on like Calico to enable communication between the pods:

```bash
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
```bash

### Step 5: Join Worker Nodes to the Cluster

On each worker node, run the kubeadm join command provided at the end of the kubeadm init process on the master node.

```bash
sudo kubeadm join <master-ip>:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```bash

### Step 6: Verify Cluster Status

Verify that all nodes have joined the cluster and are ready:

```bash
kubectl get nodes
```bash

# Deploying the LarkSuite Application

### Step 1: Apply Kubernetes Manifests

Apply the Kubernetes deployment, service, and ingress configuration files to deploy the application.

```bash
kubectl apply -f Deployment.yaml
```bash

### Step 2: Configure DNS (Optional for Local Testing)

Add an entry to /etc/hosts to access the application using the hostname defined in the Ingress resource:

```bash
<worker-node-ip> larksuite.local
```bash

### Step 3: Access the Application

After deployment, access the application via http://larksuite.local.

### Step 4: Check the Status of the Deployment

```bash
kubectl get pods
kubectl get services
kubectl get ingress
```bash
