import logging.handlers
import app
import os
from pathlib import Path

class GetLog:
    logger = None

    @classmethod
    def get_log(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger()
            cls.logger.setLevel(logging.INFO)
            file_dir = app.BASE_DIR + "/log/"
            if not os.path.exists(file_dir):
                p = Path(file_dir)
                p.mkdir(exist_ok=True)
                (p / 'log.log').open('w').write('')

            th = logging.handlers.TimedRotatingFileHandler(filename=app.BASE_DIR + "/log/log.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            th.setLevel(logging.INFO)
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            th.setFormatter(fm)
            cls.logger.addHandler(th)
        return cls.logger
