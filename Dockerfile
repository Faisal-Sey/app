FROM python:3.7-stretch
RUN apt-get update -y
RUN apt-get install python build-essential python-dev python-pip python-setuptools -y
COPY ./app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
