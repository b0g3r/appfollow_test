FROM python:3.7
MAINTAINER b0g3r
WORKDIR /opt/project
ADD Pipfile /opt/project/
ADD Pipfile.lock /opt/project/
RUN pip install --no-cache-dir pipenv==2018.5.18 && pipenv install --system
ADD . /opt/project
CMD python main.py