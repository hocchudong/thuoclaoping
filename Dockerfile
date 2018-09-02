FROM python:3.6
MAINTAINER locvu "locvx1234@gmail.com"
ENV PYTHONUNBUFFERD 1
RUN mkdir /code
RUN apt-get update && apt-get install -y supervisor fping
RUN mkdir -p /var/log/supervisor
COPY ./supervisor/supervisord.conf /etc/supervisor/conf.d/
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
CMD ["/usr/bin/supervisord"]
