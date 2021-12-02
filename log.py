from logging.config import dictConfig
import logging
import sys


class LibraryError(Exception):
    pass


class LibraryMessage(Exception):
    pass


dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})


def command(commands, *args, **kwargs):
    return commands(*args, **kwargs)

if __name__ == "__main__":
    logging.info('hello')
