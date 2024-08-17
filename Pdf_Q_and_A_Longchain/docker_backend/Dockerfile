# Use Ubuntu as the base image.
FROM ubuntu:20.04

# Set the environment variable to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive


# Install Python and necessary system dependencies.
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

# RUN apt-get update && apt-get install -y \
#     software-properties-common \
#     && add-apt-repository ppa:deadsnakes/ppa \
#     && apt-get update && apt-get install -y \
#     python3.9 \
#     python3.9-dev \
#     python3-pip \
#     && rm -rf /var/lib/apt/lists/*

# Set the working directory.
WORKDIR /app

# Copy the backend file into the /app folder.
COPY ./backend/ /app/

# Copy the data folder files inside the /app folder.
COPY ./data/ /app/data/

# COPY the requirements file and  install those.
COPY ./docker_backend/requirements.txt requirements.txt

# Copy the start file.
COPY ./docker_backend/start.sh /

# Create a virtual environment because we need to use python3.9.
# RUN python3.9 -m venv /venv
ENV PATH=/usr/bin/python3.9:$PATH
# CMD ["source", "/venv/bin/activate"]

# Install the requirements.
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

# Set the PYTHONPATH environment.
ENV PYTHONPATH ${PYTHONPATH}:/app/

# Expose the FastAPI port (usually 8000)
EXPOSE 8000

# Set the entry point.
#ENTRYPOINT ["/start.sh"]
