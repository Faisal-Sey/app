FROM python:3.6-slim-buster
RUN apt-get update -y
RUN apt-get install python build-essential python-dev python-pip python-setuptools -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
