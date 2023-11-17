# Use python:3.7 instead of slim version 
FROM python:3.7

# Set higher thread limits
ENV GUNICORN_CMD_ARGS "--threads=4"
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app 

# Copy requirements file
COPY requirements.txt .

# Install requirements one-by-one
RUN pip install pytest
# etc for each package

# Copy app
COPY sparse_recommender.py .

# Run app
CMD [ "python", "sparse_recommender.py" ]