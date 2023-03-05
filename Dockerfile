FROM python:3.9-slim-buster
MAINTAINER mehran farhadi

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

# Install Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get install -yq google-chrome-stable

# Install ChromeDriver
RUN LATEST=`curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE` \
    && wget -q https://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Install pip dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python code
COPY . .

# Set the default command to run the Python script
CMD ["python", "app.py"]