from logging.config import dictConfig
import logging


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
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    }
})


def command(commands, *args, **kwargs):
    logging.debug(commands.__name__ + ' started with args:' + str(args), ' with kwargs: ' + str(kwargs))
    try:
        return commands(*args, **kwargs)
    except LibraryMessage as m:
        logging.info(m)
        return m
    except LibraryError as e:
        logging.error(e)
        raise e
    except Exception as er:
        try:
            raise LibraryError(er)
        except LibraryError as e:
            logging.error(e)
            raise LibraryError(e)
