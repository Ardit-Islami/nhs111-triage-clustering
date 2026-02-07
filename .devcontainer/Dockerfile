FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends git curl build-essential gh && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir uv
WORKDIR /workspaces/cluster-project
