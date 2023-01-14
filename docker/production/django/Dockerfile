#pull the official base image
FROM python:3.9.8

ENV APP_BLOG=/app
RUN mkdir $APP_BLOG
RUN mkdir $APP_BLOG/staticfiles
WORKDIR $APP_BLOG

#set level
LABEL maintainer='sizanmahmud08@gmail.com'
LABEL description='Development image for a blog site'

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install dependencies
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev \
    && apt-get install -y gettext \
    && apt-get install -y netcat gcc postgresql \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements/production.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

#copy project
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start


ENTRYPOINT [ "/entrypoint" ]


EXPOSE 8009
