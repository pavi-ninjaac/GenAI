# Use Ubuntu as the base image.
FROM ubuntu:20.04

# Set the environment variable to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive


# Install Python and necessary system dependencies.
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y \
    python3.9 \
    python3.9-dev \
    python3-pip \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory.
WORKDIR /app

# Copy the backend file into the /app folder.
COPY ./backend/ /app/

# Copy the data folder files inside the /app folder.
COPY data/ /app/

# COPY the requirements file and  install those.
COPY ./docker_backend/requirements.txt requirements.txt

# Set the PYTHONPATH environment.
