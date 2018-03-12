FROM python:3-slim

WORKDIR /app

ADD . /app

RUN apt-get update

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install aws-shell

CMD ["bash"]
