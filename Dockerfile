FROM selenium/standalone-chrome
WORKDIR /app
COPY . /app
USER root
RUN mkdir -p /var/lib/apt/lists/partial
RUN chmod 755 /var/lib/apt/lists/partial
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository universe
RUN apt-get update && apt-get install -y python3-pip

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
