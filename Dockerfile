# DOCKER-VERSION 1.1.2
FROM python:3
ADD Test.py /

CMD ["python", "./Test.py"]