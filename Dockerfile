#samole docker file
# Pull the base image
FROM python:3.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set working directory
RUN mkdir /code
WORKDIR /code

#Upgrade pip
RUN pip install pip -U
ADD requirements.txt /code/

#Install dependencies
RUN pip install -r requirements.txt
ADD . /code/

#for mysql database backend
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev  -y