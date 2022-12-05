# Use the official Python image as the base image
FROM python:3.8

# create python user
RUN useradd -ms /bin/bash python

USER python

# Set the working directory to /app
WORKDIR /app

# Install the dependencies
COPY --chown=python:python requirements.txt .
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY --chown=python:python . /app


# Run the application
CMD ["python", "app.py"]
