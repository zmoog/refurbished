FROM python:3.8

WORKDIR /app

COPY . .

RUN python setup.py install

ENTRYPOINT ["rfrb"]
