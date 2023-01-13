import logging
import os
from datetime import datetime
from django.utils.log import DEFAULT_LOGGING


# LOGGING_CONFIG = None

# LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()

# logging.config.dictConfig

logger = logging.getLogger(__name__)

''' Create loggers using the logging.getLogger() factory function, so that the logging library can manage the mapping of names to instances and maintain a hierarchy of logs. This way, you can use the logger’s name to access it in different parts of the application, and only a set number of loggers will be created at runtime '''

LOG_LEVEL = 'INFO'

''' # %(asctime)s %(name)-12s %(levelname)-8s %(message)s
# asctime = define your timezone
# name = package name
# levelname = log level of message
# message = log message
# 12s & 8s = format specifications '''

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")

logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        },
        "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",},
        "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        "all_event": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "file",
            "filename": "media/log/all/"+date+".log",
        },
    },
    "loggers": {
        "all_loggers": {
            "level": "DEBUG",
            "handler": ["all_event"],
        },
    },
})