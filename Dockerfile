FROM alpine:3.11

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip


WORKDIR /app

COPY . /app
    
RUN apk add --no-cache mysql-client \
    && apk add --no-cache --virtual .build-deps gcc musl-dev mysql-dev
    
RUN pip3 --no-cache-dir install -r requirements.txt
    
CMD ["python3","app.py"]