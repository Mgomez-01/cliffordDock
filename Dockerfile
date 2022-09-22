FROM ubuntu

SHELL ["/bin/bash","-c"]

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ="America/Salt Lake City"
RUN apt-get -y update && apt-get -y install \
wget \
make \
python3-dev \
python3-numpy

RUN apt-get -y install pip \
&& pip install matplotlib  \
&& pip install clifford    \
&& pip install galgebra

RUN apt-get install -y git 