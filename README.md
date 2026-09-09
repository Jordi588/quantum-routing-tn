# quantum-routing-tn

This repository contains the implementation developed for the Master's Thesis **"Simulación Clásica mediante Redes Tensoriales: Aplicación a un Problema de Optimización de Rutas"**.

The complete environment is containerized using Docker, so no local Python installation or manual dependency configuration is required.

## Requirements

Before starting, make sure you have installed:

- Docker
- Docker Compose

## Build the Docker environment

Clone the repository and move into the project directory:

```bash
git clone git@github.com:Jordi588/quantum-routing-tn.git

cd quantum-routing-tn
```

Build the Docker image and start the JupyterLab service:

```bash
sudo docker compose -f docker-compose.yml up --build -d
```

Once the container is running, JupyterLab will be available at:

```bash
http://localhost:8888
```