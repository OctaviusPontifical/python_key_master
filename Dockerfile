FROM python:3.10.4-alpine3.16
WORKDIR /app
COPY ./ /app/
ENV DB_NAME=postgres
ENV DB_USER=mike
ENV DB_PASW=test1234
ENV DB_HOST=192.168.1.201
ENV JWT_KEY=sgjlksjgdsksg
RUN apk update \
        && apk add --virtual build-deps postgresql-dev gcc python3-dev musl-dev\
        && pip3 install -r requirements.txt
#&& apk del build-deps
CMD ["python","./main.py"]
