#Test Line
FROM python:2.7-onbuild
MAINTAINER Harsha <harshavardhanc95@gmail.com>
COPY hello-world.py /usr/src/app/hello-world.py
ENTRYPOINT ["python", "/usr/src/app/hello-world.py"]
