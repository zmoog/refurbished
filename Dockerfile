FROM python:3.13

WORKDIR /app

COPY . .

RUN python setup.py install

ENTRYPOINT ["rfrb"]
