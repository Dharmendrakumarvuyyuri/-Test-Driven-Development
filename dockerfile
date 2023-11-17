# Use python:3.7 instead of slim version 
FROM python:3.7

# Set working directory
WORKDIR /app 

# Copy app
COPY sparse_recommender.py .

# Run app
CMD [ 'pip', 'install', 'pytest', ';', "python", "sparse_recommender.py" ]