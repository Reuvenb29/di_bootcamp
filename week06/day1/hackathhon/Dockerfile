# Base image with Python
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default command to run your app
CMD ["python", "main.py"]
