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

## Deubug



When attempting to remediate pod crashes/restarts, it is important to first run the following in order to debug this properly:

```bash
kubectl get secrets --all-namespaces -o yaml
```



## Configuration

| Environment Variable     | Default                              | Description                          |
|--------------------------|--------------------------------------|--------------------------------------|
| `CONFIG_SERVICE_URL`     | `http://config-service:8888/config`  | URL of the config service            |
| `CONFIG_REFRESH_INTERVAL`| `60`                                 | Config refresh interval in seconds   |
