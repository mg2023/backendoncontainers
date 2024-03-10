FROM alpine:3.19

RUN apk -U upgrade
RUN apk add python3

ARG TZ='Chile/Continental'

ENV DEFAULT_TZ ${TZ}

RUN apk add -U tzdata \
  && cp /usr/share/zoneinfo/${DEFAULT_TZ} /etc/localtime \
  && apk del tzdata \
  && rm -rf \
  /var/cache/apk/*

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip

WORKDIR /app
#RUN mkdir -p /app/logs

COPY ./src/app.py /app
COPY ./src/requirements.txt /app
# Install dependencies:
RUN pip install -r requirements.txt

#RUN addgroup -g 1024 wgroup
#RUN adduser -D -u 1024 -G wgroup wapii
#RUN chown -R  wapii:wgroup /app
#USER wapii
EXPOSE 8000


# Run the application:
CMD ["python", "app.py"]

