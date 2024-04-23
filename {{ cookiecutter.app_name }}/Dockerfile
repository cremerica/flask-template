FROM ubuntu:20.04

MAINTAINER  {{cookiecutter.email}}

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./Requirements.txt /Requirements.txt

WORKDIR /

RUN pip3 install -r Requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "app/app.py" ]
