FROM selenium/standalone-chrome
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y python-pip
RUN pip install -r requirements.txt
CMD ["python", "main.py"]