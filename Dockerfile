# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#needed for postgresql?
RUN apt-get update && apt-get install -y build-essential cmake 
RUN apt-get install libopenblas-dev liblapack-dev -y
RUN apt-get install libx11-dev libgtk-3-dev -y
RUN apt-get install postgresql postgresql-contrib -y

# Set the working directory in the container to /app
WORKDIR /app
COPY requirements.txt requirements.txt
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Add the current directory files (on your machine) to the container
ADD /app/ /app/

COPY requirements.txt requirements.txt

# Expose the port server is running on
EXPOSE 8000

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

