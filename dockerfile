# Use an official Python runtime as the base image
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container 
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the main.py script to the container
COPY sparse_recommender.py .

# Define the command to run when starting the container
CMD ["python", "sparse_recommender.py"]