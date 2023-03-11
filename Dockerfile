FROM selenium/standalone-chrome
WORKDIR /app
COPY . /app
RUN mkdir -p /var/lib/apt/lists/partial
RUN chmod 755 /var/lib/apt/lists/partial
RUN apt-get update && apt-get install -y python-pip
RUN pip install -r requirements.txt
CMD ["python", "main.py"]