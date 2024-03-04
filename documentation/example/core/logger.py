import logging
import logging.handlers
import os
from datetime import datetime
from logging import Formatter, Handler, Logger
from typing import NoReturn, Union

import requests

from core.config import config


def send_telegram_message(token: str, chat_ids: list[int], message: str):
    print(f"chat_ids: {chat_ids}")
    for chat_id in chat_ids:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {"chat_id": chat_id, "text": message, "parse_mode": "HTML"}
        logging.info(f"params: {params}")
        response = requests.post(url=url, params=params)
        logging.info(f"Response {response.status_code}: {response.text}")


class TelegramHandler(logging.Handler):
    """
    Handler для того, чтобы отправлять telegram сообщения при логгировании

    Note:
        Не включайте `self` параметра в ``Args`` секцию.

    Args:
        token (str): Токен для бота
        chat_ids (list[int]): Список chat_id куда отправлять

    Attributes:
        token (str): Токен для бота
        chat_ids (list[int]): Список chat_id куда отправлять
    """
    def __init__(self, token: str, chat_ids: list[int]):
        super().__init__()
        self.token = token
        self.chat_ids = chat_ids
        print(chat_ids)

    def emit(self, record: logging.LogRecord):
        log_entry = self.format(record)
        send_telegram_message(self.token, self.chat_ids, log_entry)


class AdvLogger:
    """
    Класс для логгирование работы приложения, использует logging

    Args:
        logger_name (str): Имя логгера

    Attributes:
        logger_name (str): Имя логгера

    """

    def __init__(self, logger_name: str):
        self.logger: Logger = logging.getLogger(logger_name)
        message_format: str = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        formatter: Formatter = logging.Formatter(message_format)
        self.logger.setLevel(logging.DEBUG)

        stream_handler: Handler = self.init_handler(
            handler_class=logging.StreamHandler(),
            formatter=formatter,
            level=logging.DEBUG,
        )
        """
        Базовые handler для записи в консоль
        """

        current_date = datetime.now().strftime("%Y_%m_%d")
        log_filename = os.path.join(config.PATH_LOG, f"log_{current_date}.log")
        file_handler: Handler = self.init_handler(
            handler_class=logging.handlers.RotatingFileHandler(
                filename=log_filename, maxBytes=1048576, backupCount=5
            ),
            formatter=formatter,
            level=logging.INFO,
        )
        """
        Базовые handler для записи в файлы
        """

        telegram_handler: Handler = self.init_handler(
            handler_class=TelegramHandler(config.BOT_TOKEN, config.CHAT_IDS),
            formatter=formatter,
            level=logging.WARNING,
        )
        """
        Самописный handler для отправки сообщения в telegram
        """

        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(telegram_handler)
        self.logger.debug("logger init")

    def init_handler(
        self, handler_class: Handler, formatter: Formatter, level: int
    ) -> Handler:
        handler = handler_class
        handler.setFormatter(formatter)
        handler.setLevel(level)
        return handler

    def write_log(self, level: str, msg: str) -> NoReturn:
        """
        Написание сообщения во все имеющиеся handler в зависимости от назначенного уровня испольнения

        Notes:
            * Уровни используются из стандартной библиотеки ``logging``
            * ``level`` передавать строкой

        Examples:
            Пример написания лога на уровне INFO

            >>> loggerObject.write_log("INFO", "Начало выполнения фукнции example")

        Args:
            level (str): Уровень сообщения
            msg (str): Текст сообщения
        """
        self.logger.log(level=eval(f"logging.{level}"), msg=msg)
