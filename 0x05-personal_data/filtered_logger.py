#!/usr/bin/env python3
""" Contain a class and several functions """

from typing import List
import re
import os
import logging
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initialization of data """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filter values for incoming lof """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ returns the log message obfuscated """
    for field in fields:
        message = re.sub(f'(?<={field}=)[^{separator}]*', redaction, message)
    return message


def get_logger() -> logging.Logger:
    """ returns a logging.Logger object """
    log = logging.getLogger('user_data')
    log.setLevel(logging.INFO)
    log.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    log.addHandler(stream_handler)
    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ returns a connector to the database """
    connector = mysql.connector.connect(
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME')
    )
    return connector


def main() -> None:
    """ main function """
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users;')
    logger = get_logger()
    for row in cursor:
        logger.log(logging.INFO, row[0])
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
