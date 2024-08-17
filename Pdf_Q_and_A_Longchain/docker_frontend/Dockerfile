# Use node as the base image.
FROM node:18 as build

# Set the working directory.
WORKDIR /app

# Copy the backend file into the /app folder.
COPY ./front_end/frontend/ /app/

# COPY the requirements file and  install those.
RUN npm install
RUN npm install axios
RUN npm install sass
RUN npm install react-dropzone

# Expose the port (usually 8080)
EXPOSE 3000

# Copy the start file.
COPY ./docker_frontend/start.sh /

# Set the entry point.
ENTRYPOINT ["/start.sh"]
