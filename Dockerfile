FROM centos:latest

MAINTAINER VITOR LIMA DE LAVOR

RUN ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

RUN mkdir /app

WORKDIR /app

RUN yum repolist

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm

RUN yum install -y python36u python36u-libs python36u-devel python36u-pip 

COPY rundasa/* /app/

RUN pip3.6 install -r requirements.txt

EXPOSE 50000

ENTRYPOINT [ "python3.6", "app.py", "runserver"]





