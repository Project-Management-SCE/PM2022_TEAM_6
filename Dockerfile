

FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /requirements.txt
COPY ./School /code
COPY ./manager .
COPY ./voulnteers .
COPY ./coordinator .
COPY ./mainpage .
COPY ./tests .
EXPOSE 8000
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app \
RUN /py/bin/python -m pip install "pymongo[srv]"

ENV PATH="/py/bin:$PATH"
USER app
RUN apt-get -y install docker-ce
RUN apt-get install npm
RUN npm install jshint
RUN npm install csslint

