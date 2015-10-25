# Author: Tran Huu Cuong
#
# Build: docker build -t tranhuucuong91/simple-blog:0.1 .
# Run: docker run -d -p 15000:5000 --name simple-blog-run tranhuucuong91/simple-blog:0.1
#

FROM tranhuucuong91/python:3.4
MAINTAINER Tran Huu Cuong "tranhuucuong91@gmail.com"

# using apt-cacher-ng proxy for caching deb package
#RUN echo 'Acquire::http::Proxy "http://172.17.42.1:3142/";' > /etc/apt/apt.conf.d/01proxy

#ENV REFRESHED_AT 2015-10-22

#RUN apt-get update -qq
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -y zsh

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY . /app

#ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5000
CMD ["/app/run.py"]

