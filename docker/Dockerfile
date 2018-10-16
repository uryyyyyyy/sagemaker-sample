# docker build --tag 149721313133.dkr.ecr.ap-northeast-1.amazonaws.com/sagemaker-example:0.1 ./
# docker push 149721313133.dkr.ecr.ap-northeast-1.amazonaws.com/sagemaker-example:0.1

FROM ubuntu:18.04

# apt update
RUN apt-get update

# timezone
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ='Asia/Tokyo'
RUN set -x && \
  echo $TZ > /etc/timezone && \
  apt-get install -y wget software-properties-common

RUN set -x && \
  add-apt-repository ppa:jonathonf/python-3.6 && \
  apt-get update && \
  apt-get install -y python3.6 python3.6-dev python3-distutils && \
  wget https://bootstrap.pypa.io/get-pip.py && \
  python3.6 get-pip.py && \
  ln -s /usr/bin/python3.6 /bin/python

# library install
ADD ./requirements.txt /requirements.txt
RUN set -x && \
  pip install -r /requirements.txt

# set train command
ADD ./train /bin/train
RUN set -x && \
  chmod +x /bin/train
ADD ./train.py /train.py

# set serve command
ADD ./serve /bin/serve
RUN set -x && \
  chmod +x /bin/serve
ADD ./serve.py /serve.py
