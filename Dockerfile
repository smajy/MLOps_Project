# Base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY ./deploy .

# Expose the port on which the application will run
EXPOSE 5000

# Define the command to run the application
CMD ["python", "deploy.py"]
