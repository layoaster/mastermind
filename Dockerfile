FROM python:3.6.3-alpine3.6

LABEL maintainer="Lionel Mena <lionelmena@gmail.com>"

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code

RUN set -x \
    && pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

COPY ./docker-entrypoint.sh /

# CMD ["/bin/sleep", "100000"]
CMD ["/docker-entrypoint.sh"]