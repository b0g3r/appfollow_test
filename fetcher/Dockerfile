FROM python:3.7

MAINTAINER b0g3r
WORKDIR /opt/project

RUN groupadd -r pythonuser && useradd -r -g pythonuser pythonuser
RUN mkdir /opt/pictures && chown pythonuser:pythonuser /opt/pictures
VOLUME /opt/pictures

ADD poetry.lock pyproject.toml /opt/project/

RUN pip install --no-cache-dir "poetry>=1.0.0" && \
    poetry config virtualenvs.create false && \
    poetry install

ADD . /opt/project

RUN chown -R pythonuser:pythonuser /opt/project
USER pythonuser

CMD python main.py