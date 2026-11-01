FROM python:3.15

WORKDIR /app

COPY . .

RUN python setup.py install

ENTRYPOINT ["rfrb"]
