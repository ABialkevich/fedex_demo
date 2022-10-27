FROM python:3.11.0-slim

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY . /src/

COPY hub_healthcheck.sh /src/
CMD ["hub_healthcheck.sh"]