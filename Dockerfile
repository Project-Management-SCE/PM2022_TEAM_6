

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
    adduser --disabled-password --no-create-home app
    
ENV PATH="/py/bin:$PATH"

CMD ["python","-c","print('Hi There')"]
