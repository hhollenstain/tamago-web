FROM python:3.6-alpine

COPY . /app
WORKDIR /app

RUN apk add gcc musl-dev libffi-dev
RUN pip install -e "."

CMD ["tamago_web"]
