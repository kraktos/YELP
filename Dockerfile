# DOCKER-VERSION 1.1.2
# define the python version
FROM python:2.7

# install dependencies
RUN pip install --no-cache-dir pandas
RUN pip install --no-cache-dir nltk

# copy all to a directory
COPY . /src

# set it as a working directory
WORKDIR /src

# set python bufferring to false
ENV PYTHONUNBUFFERED 0

# execute the command to run the program
CMD ["python", "Main.py"]