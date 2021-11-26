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
    logging.info(str(commands.__name__) + ' started with args:' + str(args), ' with kwargs: ' + str(kwargs))
    try:
        return commands(*args, **kwargs)
    except LibraryMessage as m:
        logging.info(m)
        return m
    except LibraryError as e:
        logging.info(str(e) + ' 오류가 발생하였습니다.')
    except Exception as er:
        try:
            raise LibraryError(er)
        except LibraryError as e:
            logging.info(str(e) + ' 오류가 발생하였습니다.')


if __name__ == "__main__":
    logging.info('hello')
