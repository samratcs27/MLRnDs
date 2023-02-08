FROM <aws-emr-base-docker-xyz>/<zzz-base>:latest
RUN apt-get update && apt-get update -y
ADD . /app
WORKDIR /app
RUN dos2unix scripts/start.sh
RUN dos2unix scripts/build.sh && sh scripts/build.sh
CMD ["sh", "scripts/start.sh"]