FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -yq \
    wget \
    curl \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    && rm -rf /var/lib/apt/lists/*

# Install pip dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python code
COPY . .

# Set the default command to run the Python script
CMD ["python", "app.py"]