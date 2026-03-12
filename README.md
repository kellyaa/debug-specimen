# debug-specimen

A minimal Python application.

## What it does

A Flask HTTP server with two endpoints:

- `GET /` — returns a greeting and the current uptime
- `GET /healthz` — healthcheck.


## Project structure

```
app.py             Flask application
requirements.txt   Python dependencies
Dockerfile         Container image build
deployment.yaml    Kubernetes Deployment manifest
```

## Prerequisites

- Docker
- A local Kubernetes cluster (minikube, kind, or Docker Desktop)
- kubectl

## Usage

Build the container image:

```bash
docker build -t debug-specimen:latest .
```

Deploy to your cluster:

```bash
kubectl apply -f deployment.yaml
```

Check the liveness probe failures in the events:

```bash
kubectl describe pod -l app=debug-specimen
```

View application logs:

```bash
kubectl logs -l app=debug-specimen --follow
```

## Addressing deployment issues

1. Delete the entire namespace where it resides: - `kubectl delete namespace <namespace>`
