+++
title = "Deploy Traefik as a reverse proxy with Kubernetes"
description = "Deploy Traefik as a reverse proxy with Kubernetes"
date = 2025-05-25T00:00:00Z
draft = false
aliases = ["fr/tutorial/kubernetes"]

[taxonomies]
tags = ["Features","kubernetes", "Reverse proxy", "Nginx", "Traefik"]
categories = ["Software"]
[extra]
keywords = "Kubernetes, Reverse proxy, Nginx, Traefik"
toc = true
series = "Features"
+++

# Deploy Traefik as a reverse proxy with Kubernetes

I recommend learning the basics of Docker/containers and Kubernetes before starting this tutorial.

## Dependencies and configure Kubernetes

Install the required packages for Kubernetes and Minikube on your system:

On **Arch Linux/Manjaro**:

```bash
sudo pacman -S minikube cri-o kompose helm kubectl kubelet kubeadm
```

start minikube:

```bash
minikube start
```

Configure Kubernetes context to use Minikube:

```bash
kubectl config use-context minikube && kubectl config get-contexts && kubectl get nodes
```

Enable and start kubelet service:

```bash
sudo systemctl start kubelet && sudo systemctl enable --now kubelet && sudo systemctl status kubelet
```

## Deploy Traefik with Helm

Let's deploy Traefik using Helm, which is a package manager for Kubernetes.

```bash
helm repo add traefik https://traefik.github.io/charts && helm repo update && helm install traefik traefik/traefik --namespace traefik-tutorial --create-namespace
```

Once the installation is complete, you can check the status of the traefik install:

```bash
helm list -A
```

Result:

```bash
NAME    NAMESPACE               REVISION        UPDATED                                 STATUS          CHART           APP VERSION
traefik traefik-tutorial        1               2025-05-27 21:55:44.32763531 +0200 CEST deployed        traefik-35.2.0  v3.3.6
```

You can also check the status of services:

```bash
minikube service list
```

You should see output similar to this:

```bash
|------------------|-----------------|---------------|---------------------------|
|    NAMESPACE     |      NAME       |  TARGET PORT  |            URL            |
|------------------|-----------------|---------------|---------------------------|
| default          | kubernetes      | No node port  |                           |
| kube-system      | kube-dns        | No node port  |                           |
| traefik-tutorial | traefik         | web/80        | http://192.168.49.2:31134 |
|                  |                 | websecure/443 | http://192.168.49.2:32083 |
|------------------|-----------------|---------------|---------------------------|
```

The **NAME** (*traefik*) must match to **ingressClassName** in the Ingress controller.

You can also check the ingress controller:

```bash
kubectl get ingressclass
```

Result:

```bash
NAME      CONTROLLER                      PARAMETERS   AGE
traefik   traefik.io/ingress-controller   <none>       34h
```

Get the Traefik service URL:

```bash
minikube service traefik -n traefik-tutorial --url
```

Result:

```bash
http://192.168.49.2:31134
http://192.168.49.2:32083
```

You can check `traefik` pod in the `traefik-tutorial` namespace:

```bash
kubectl get pods --all-namespaces
```

Result:

```bash
NAMESPACE          NAME                               READY   STATUS    RESTARTS       AGE
kube-system        coredns-668d6bf9bc-4wnlv           1/1     Running   5 (22h ago)    9d
kube-system        etcd-minikube                      1/1     Running   5 (22h ago)    9d
kube-system        kube-apiserver-minikube            1/1     Running   5 (22h ago)    9d
kube-system        kube-controller-manager-minikube   1/1     Running   5 (22h ago)    9d
kube-system        kube-proxy-79r5k                   1/1     Running   5 (22h ago)    9d
kube-system        kube-scheduler-minikube            1/1     Running   5 (22h ago)    9d
kube-system        storage-provisioner                1/1     Running   12 (30m ago)   9d
traefik-tutorial   traefik-66c954b954-qzdvw   1/1     Running   0              4m35s
```

## Deploy a sample application with Traefik

You can now deploy a sample application to test Traefik as a reverse proxy, we will deploy the `whoami` application, which is a simple HTTP server that returns information about the request it receives.

**traefik.ingress.whoami.yml** : Ingress define to route traffic to the `whoami` service.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: whoami-ingress
  namespace: traefik-tutorial
  annotations:
      #kubernetes.io/ingress.class: traefik
      traefik.ingress.kubernetes.io/router.entrypoints: web
      #traefik.ingress.kubernetes.io/router.entrypoints: websecure
spec:
  ingressClassName: traefik
  rules:
    - host: whoami.bensuperpc.org
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: whoami
                port:
                  number: 80
    - host: whoami.192.168.49.2.nip.io
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: whoami
                port:
                  number: 80
```

**whoami.deployment.yml** : The Deployment specifies how the `whoami` application runs inside a pod.

```yaml
kind: Deployment
apiVersion: apps/v1
metadata:
  name: whoami
  namespace: traefik-tutorial
  labels:
    app: whoami

spec:
  replicas: 1
  selector:
    matchLabels:
      app: whoami
  template:
    metadata:
      labels:
        app: whoami
    spec:
      containers:
        - name: whoami
          image: traefik/whoami
          ports:
            - name: web
              containerPort: 80
```

**whoami.services.yml** : The Service specifies how the application is made accessible on the network.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: whoami
  namespace: traefik-tutorial

spec:
  type: ClusterIP
  ports:
    - name: web
      port: 80
      targetPort: 80
  selector:
    app: whoami
```

Apply the Ingress, Deployment, and Service configurations:

```bash
kubectl apply -f whoami.services.yml -f whoami.deployment.yml -f traefik.ingress.whoami.yml
```

Check the status of the pods to ensure they are running:

```bash
kubectl get pods --all-namespaces
```

You should see `whoami` and `traefik` pods running in the `traefik-tutorial` namespace:

```bash
NAMESPACE          NAME                               READY   STATUS    RESTARTS      AGE
kube-system        coredns-668d6bf9bc-5llhm           1/1     Running   2 (10h ago)   34h
kube-system        etcd-minikube                      1/1     Running   2 (10h ago)   34h
kube-system        kube-apiserver-minikube            1/1     Running   2 (10h ago)   34h
kube-system        kube-controller-manager-minikube   1/1     Running   2 (10h ago)   34h
kube-system        kube-proxy-9llmn                   1/1     Running   2 (10h ago)   34h
kube-system        kube-scheduler-minikube            1/1     Running   2 (10h ago)   34h
kube-system        storage-provisioner                1/1     Running   5 (30s ago)   34h
traefik-tutorial   traefik-66c954b954-qzdvw           1/1     Running   2 (10h ago)   34h
traefik-tutorial   whoami-68965c9df8-cv94z            1/1     Running   2 (10h ago)   34h
```

Now you can access the `whoami` service through Traefik using the defined hostnames:

```bash
curl -H "Host: whoami.bensuperpc.org" http://192.168.49.2:31134
```

Result:

```bash
Hostname: whoami-68965c9df8-cv94z
IP: 127.0.0.1
IP: ::1
IP: 10.244.0.4
IP: fe80::90a3:81ff:fe9d:8107
RemoteAddr: 10.244.0.6:48226
GET / HTTP/1.1
Host: whoami.bensuperpc.org
User-Agent: curl/8.13.0
Accept: */*
Accept-Encoding: gzip
X-Forwarded-For: 10.244.0.1
X-Forwarded-Host: whoami.bensuperpc.org
X-Forwarded-Port: 80
X-Forwarded-Proto: http
X-Forwarded-Server: traefik-686745597f-g49dt
X-Real-Ip: 10.244.0.1
```

If you access with your browser to `http://whoami.192.168.49.2.nip.io:31134/`, you should see the same result.

*You may need to add the `whoami.192.168.49.2.nip.io` and `whoami.bensuperpc.org` domains to your `/etc/hosts` file or use a DNS service that resolves it to the Minikube IP address.*

## Scaling the application

We can now add more whoami instances, and Traefik will route the traffic automatically based on the Ingress rules defined.

Let's scale the `whoami` deployment to 5 replicas:

```bash
kubectl scale deploy whoami --replicas=5 -n traefik-tutorial 
```

Now check the status of the pods again:

```bash
kubectl get pods --all-namespaces
```

You should see multiple `whoami` pods running:

```bash
NAMESPACE          NAME                               READY   STATUS    RESTARTS      AGE
kube-system        coredns-668d6bf9bc-5llhm           1/1     Running   2 (10h ago)   34h
kube-system        etcd-minikube                      1/1     Running   2 (10h ago)   34h
kube-system        kube-apiserver-minikube            1/1     Running   2 (10h ago)   34h
kube-system        kube-controller-manager-minikube   1/1     Running   2 (10h ago)   34h
kube-system        kube-proxy-9llmn                   1/1     Running   2 (10h ago)   34h
kube-system        kube-scheduler-minikube            1/1     Running   2 (10h ago)   34h
kube-system        storage-provisioner                1/1     Running   5 (30s ago)   34h
traefik-tutorial   traefik-66c954b954-qzdvw           1/1     Running   2 (10h ago)   34h
traefik-tutorial   whoami-68965c9df8-cv94z            1/1     Running   2 (10h ago)   34h
traefik-tutorial   whoami-68965c9df8-5g7xk            1/1     Running   0             2m
traefik-tutorial   whoami-68965c9df8-7j5qk            1/1     Running   0             2m
traefik-tutorial   whoami-68965c9df8-8j6xk            1/1     Running   0             2m
traefik-tutorial   whoami-68965c9df8-9k7xk            1/1     Running   0             2m
```

You can access the `whoami` service again, and it will now return responses from different pods, demonstrating that Traefik is load balancing the requests across the replicas.

```bash
curl -H "Host: whoami.bensuperpc.org" http://192.168.49.2:31134
```

`Hostname` and `IP` will change each time you call the service, as it will return the information from a different pod.

Rescale the `whoami` deployment back to 1 replica:

```bash
kubectl scale deploy whoami --replicas=1 -n traefik-tutorial 
```

### Horizontal Pod Autoscaler

You need to install the metrics server to use HPA. You can install it with the following command:

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

Now update your `whoami` deployment to use HPA to automatically scale the number of replicas.

**whoami.deployment.yml**

```yaml
kind: Deployment
apiVersion: apps/v1
metadata:
  name: whoami
  namespace: traefik-tutorial
  labels:
    app: whoami

spec:
  replicas: 1
  selector:
    matchLabels:
      app: whoami
  template:
    metadata:
      labels:
        app: whoami
    spec:
      containers:
        - name: whoami
          image: traefik/whoami
          ports:
            - name: web
              containerPort: 80
          resources:
            requests:
              cpu: "100m"
              memory: "128Mi"
            limits:
              cpu: "250m"
              memory: "256Mi"
```

Add the Horizontal Pod Autoscaler configuration to automatically scale the `whoami` deployment.

**whoami.hpa.yml**

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: whoami
  namespace: traefik-tutorial
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: whoami
  minReplicas: 1
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 50
```

Apply the updated `whoami` deployment and HPA configuration:

```bash
kubectl apply -f whoami.services.yml -f whoami.deployment.yml -f traefik.ingress.whoami.yml -f whoami.hpa.yml
```

Now you can check the status of the Horizontal Pod Autoscaler:

```bash
kubectl get hpa -n traefik-tutorial
```

Expected result:

```bash
NAME     REFERENCE           TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
whoami   Deployment/whoami   cpu: <unknown>/50%   1         5         1          85s
```

## Clean up

To clean up the resources created during this tutorial, you can delete the Ingress, Deployment, and Service configurations, as well as the Traefik installation.

Uninstall helm chart:

```bash
helm uninstall traefik --namespace traefik-tutorial
```

Delete all resources in the `traefik-tutorial` namespace and cleanup Minikube:

```bash
kubectl delete all --all -n traefik-tutorial && minikube delete
```

More info:

- [Traefik documentation](https://doc.traefik.io/traefik/)
- [Traefik quick start](https://doc.traefik.io/traefik/getting-started/quick-start-with-kubernetes/)
- [Difference clusterip/nodeport/loadbalancer](https://octopus.com/blog/difference-clusterip-nodeport-loadbalancer-kubernetes)
- [Voting application example](https://github.com/dockersamples/example-voting-app)
- [api gateway autoscaling](https://doc.traefik.io/traefik-hub/api-gateway/expose/api-gateway-autoscaling)