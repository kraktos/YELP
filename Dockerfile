# DOCKER-VERSION 1.1.2
# define the python version
FROM python:3

# install dependencies
RUN pip install --no-cache-dir pandas

# copy all to a directory
COPY . /src

# set it as a working directory
WORKDIR /src

# execute the command to run the program
CMD ["python", "Test.py"]