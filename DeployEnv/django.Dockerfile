FROM python:3.8.5

MAINTAINER CHO

WORKDIR /home/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

EXPOSE 8000