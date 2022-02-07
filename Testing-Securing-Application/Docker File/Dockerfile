# Use python:alpine3.7 for the base image

FROM python:alpine3.7

# Copy the .py files in ./app from build's context to /app

COPY ./app/*.py /app 

# Copy the Pipfile in ./app from build's context to /app

COPY ./app/Pipfile /app

# Change the working directory to WORKDIR

WORKDIR /app

# Install bind-tools

RUN apk add-bind-tools

# Install pipenv

RUN pip install pipenv

RUN pip install django
# Install the environment


# Expose port 8080


# Start the python application

