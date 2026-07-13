# Approved, strictly pinned Ubuntu base image
FROM ubuntu:22.04@sha256:aabed3296a3d4d443e2e07aa4b4cfcf7f1e9c2f6d2e61a68759a22f36f6630f9

# Install core dependencies needed for the runtime environment
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-pytest \
    && rm -rf /var/lib/apt/lists/*

# Set up work directory
WORKDIR /workspace

# Copy task files securely
COPY . /workspace
