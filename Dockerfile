FROM python:3.10.4-alpine3.16
WORKDIR /app
COPY ./ /app/
ENV DB_NAME=DbName
ENV DB_USER=DbUser
ENV DB_PASW=DbPassword
ENV DB_HOST=DbIp_Dm
ENV JWT_KEY=Skey
RUN pip3 install -r requirements.txt
CMD ["python","./main.py"]
