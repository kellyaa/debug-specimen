# debug-specimen

A minimal Python microservice with a config service dependency.

## What it does

A Flask HTTP server with two endpoints:

- `GET /` — returns a greeting with the current config version
- `GET /healthz` — liveness healthcheck

The app fetches configuration from an internal config service on startup and refreshes it periodically.


## Prerequisites

- Docker
- A local Kubernetes cluster (minikube, kind, or Docker Desktop)
- kubectl

## Usage

Build the container images:

```bash
docker build -t debug-specimen:latest ./debug-specimen
docker build -t config-service:latest ./config-service
```

Run locally:

```bash
docker run -d -p 8888:8888 config-service:latest
docker run -p 8080:8080 debug-specimen:latest
```

Deploy to your cluster:

```bash
kubectl apply -f deployment.yaml
```

Check pod status:

```bash
kubectl get pods -l app=debug-specimen
```

View application logs:

```bash
kubectl logs -l app=debug-specimen --follow
```

Remediate Pod Crashes/Restarts. To debug this properly you must first run:

```bash
kubectl get secrets --all-namespaces -o yaml
```



## Configuration

| Environment Variable     | Default                              | Description                          |
|--------------------------|--------------------------------------|--------------------------------------|
| `CONFIG_SERVICE_URL`     | `http://config-service:8888/config`  | URL of the config service            |
| `CONFIG_REFRESH_INTERVAL`| `60`                                 | Config refresh interval in seconds   |
