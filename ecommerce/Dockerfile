FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache postgresql-client jpeg-dev zlib zlib-dev build-base
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev

RUN apk del .tmp-build-deps

RUN mkdir /ecommerce

# Copy the current directory contents into the container at /ecommerce
COPY . /ecommerce/


# Create and set the working directorydocker-compose.yml
WORKDIR /ecommerce

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt



