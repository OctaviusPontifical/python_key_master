FROM alpine:3.16
WORKDIR /
COPY ./ /
ENV DB_NAME=
ENV DB_USER=
ENV DB_PASW=
ENV DB_HOST=
ENV JWT_KEY=
CMD python3 ./main.py