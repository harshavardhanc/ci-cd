#Test Line
FROM python:2.7-onbuild
MAINTAINER Harsha
COPY hello-world.py /usr/src/app/hello-world.py
ENTRYPOINT ["python", "/usr/src/app/hello-world.py"]
