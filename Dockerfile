FROM python:3.14

WORKDIR /app

COPY . .

RUN python setup.py install

ENTRYPOINT ["rfrb"]
