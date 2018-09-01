# BUILD Stage
FROM alpine:latest AS builder

LABEL maintainer="imquanquan <imquanquan99@gmail.com>"

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \ 
        apk update && apk add --no-cache git && rm -rf /var/cache/apk/* && \
        git clone https://github.com/imquanquan/bookmarks.git 


FROM alpine:latest

COPY ./pip.conf /root/.pip/pip.conf
COPY --from=builder /bookmarks /var/www/bookmarks
COPY ./settings.py /var/www/bookmarks/bookmarks/settings.py

WORKDIR /var/www/bookmarks

ENV LIBRARY_PATH=/lib:/usr/lib

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    apk update && apk add build-base python3-dev py3-cryptography make py3-pip jpeg-dev zlib-dev libffi-dev openssl-dev linux-headers ca-certificates gcc && \
    pip3 install -r requirements.txt && \
    python3 manage.py collectstatic 
    
CMD gunicorn bookmarks.wsgi:application -b 0.0.0.0:8000 --reload

