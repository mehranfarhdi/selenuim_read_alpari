FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y wget gnupg2
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable

RUN apt-get install -y curl unzip
RUN curl -s https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_linux64.zip > /tmp/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver_linux64.zip chromedriver -d /usr/local/bin/

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

COPY script.py /app/


# Set the default command to run the Python script
CMD [ "python", "script.py" ]
