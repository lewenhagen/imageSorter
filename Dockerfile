FROM python:3.7.2-slim-stretch

RUN apt-get update \
    && apt-get install -y \
    tree \
    python3-setuptools \
    libtiff5-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    tcl8.5-dev \
    tk8.5-dev \
    && pip3 install Pillow \
    python-magic


ADD *.py ./

ENTRYPOINT ["python3"]

CMD ["main.py"]
